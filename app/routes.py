from flask import Blueprint, render_template
from app.models import db, Service

bp = Blueprint("main", __name__)


@bp.route("/")
def accueil():
    services = db.session.execute(
        db.select(Service).order_by(Service.categorie, Service.prix_cents)
    ).scalars().all()
    return render_template("accueil.html", services=services)