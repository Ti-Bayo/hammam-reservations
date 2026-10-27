import click
from app.models import db, Service

SERVICES = [
    ("Accès au hammam", "hammam", 90, 4500),
    ("Gommage corps complet au savon noir", "gommage", 30, 3000),
    ("Gommage du dos", "gommage", 10, 1500),
    ("Enveloppement à l'argile (rhassoul)", "enveloppement", 20, 5000),
    ("Masque du visage", "masque", 10, 3500),
    ("Masque du corps", "masque", 15, 4000),
    ("Épilation des sourcils", "epilation", 15, 1500),
    ("Épilation des aisselles", "epilation", 15, 2000),
    ("Épilation du maillot", "epilation", 20, 3000),
    ("Épilation des demi-jambes", "epilation", 30, 3500),
    ("Épilation des jambes complètes", "epilation", 45, 5500),
]


@click.command("init-db")
def init_db_command():
    """Recrée la base de données et ajoute les services."""
    db.drop_all()
    db.create_all()
    for nom, categorie, duree, prix in SERVICES:
        db.session.add(Service(nom=nom, categorie=categorie,
                               duree_minutes=duree, prix_cents=prix))
    db.session.commit()
    click.echo(f"Base créée avec {len(SERVICES)} services.")