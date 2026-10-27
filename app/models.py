from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    categorie = db.Column(db.String(30), nullable=False)
    duree_minutes = db.Column(db.Integer, nullable=False)
    prix_cents = db.Column(db.Integer, nullable=False)
    actif = db.Column(db.Boolean, default=True)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    courriel = db.Column(db.String(120), nullable=False)
    telephone = db.Column(db.String(20))
    reservations = db.relationship("Reservation", back_populates="client")


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)
    debut = db.Column(db.DateTime, nullable=False)
    nb_personnes = db.Column(db.Integer, default=1)
    statut = db.Column(db.String(20), default="confirmee")
    creee_le = db.Column(db.DateTime, default=datetime.now)

    client = db.relationship("Client", back_populates="reservations")
    service = db.relationship("Service")