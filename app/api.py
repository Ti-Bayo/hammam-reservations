from datetime import datetime
from flask import Blueprint, jsonify, request
from app.models import db, Service, Client, Reservation

api = Blueprint("api", __name__, url_prefix="/api")


def service_en_json(s):
    return {
        "id": s.id,
        "nom": s.nom,
        "categorie": s.categorie,
        "duree_minutes": s.duree_minutes,
        "prix_cents": s.prix_cents,
    }


@api.get("/services")
def liste_services():
    services = db.session.execute(
        db.select(Service).where(Service.actif)
    ).scalars().all()
    return jsonify([service_en_json(s) for s in services])


@api.get("/services/<int:service_id>")
def detail_service(service_id):
    service = db.get_or_404(Service, service_id)
    return jsonify(service_en_json(service))


@api.get("/reservations/<int:reservation_id>")
def detail_reservation(reservation_id):
    reservation = db.get_or_404(Reservation, reservation_id)
    return jsonify({
        "id": reservation.id,
        "client": reservation.client.nom,
        "service": reservation.service.nom,
        "debut": reservation.debut.isoformat(),
        "statut": reservation.statut,
    })


@api.post("/reservations")
def creer_reservation():
    donnees = request.get_json(silent=True) or {}

    manquants = [c for c in ["nom", "courriel", "service_id", "debut"] if not donnees.get(c)]
    if manquants:
        return jsonify({"erreur": f"Champs manquants : {', '.join(manquants)}"}), 400

    service = db.session.get(Service, donnees["service_id"])
    if service is None:
        return jsonify({"erreur": "Service introuvable"}), 404

    try:
        debut = datetime.fromisoformat(donnees["debut"])
    except ValueError:
        return jsonify({"erreur": "Date invalide (exemple : 2027-01-16T13:00)"}), 400

    # Étape 4 : a ajouter les règles métier
    # (heures d'ouverture, 10 personnes par plage, 2 soins en même temps)

    client = Client(nom=donnees["nom"], courriel=donnees["courriel"],
                    telephone=donnees.get("telephone"))
    reservation = Reservation(client=client, service=service, debut=debut,
                              nb_personnes=donnees.get("nb_personnes", 1))
    db.session.add(reservation)
    db.session.commit()

    return jsonify({
        "id": reservation.id,
        "service": service.nom,
        "debut": reservation.debut.isoformat(),
        "statut": reservation.statut,
    }), 201