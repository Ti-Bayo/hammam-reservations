# Les Bains D'Argile – Application de réservations

Application web de gestion des réservations pour un hammam (entreprise fictive), développée avec Flask.

## Contexte

En travaillant comme réceptionniste dans un hammam, j'ai observé les besoins concrets de la gestion des réservations : capacité limitée du hammam, nombre restreint de salles de soins, horaires différents la semaine et la fin de semaine. Ce projet propose une solution à ces contraintes. Les noms, services et prix sont fictifs.

## Fonctionnalités

- [x] Catalogue des services (hammam, gommages, enveloppements, masques, épilation)
- [x] Base de données des clients, des services et des réservations
- [ ] Réservation en ligne avec choix du service, de la date et de la plage horaire
- [ ] Règles de capacité : 10 personnes par plage au hammam, 2 soins en simultané, 2 soins maximum par client et par visite
- [ ] Espace employé : réservations du jour, annulation
- [ ] Tests automatisés (pytest)
- [ ] Mise en ligne

## Technologies

Python · Flask · Flask-SQLAlchemy · SQLite · Jinja2 · Bootstrap 5 · pytest

## Règles métier

| Règle | Valeur |
|---|---|
| Heures d'ouverture | Semaine : 10 h à 16 h 30 · Fin de semaine : 11 h à 21 h 30 |
| Plages du hammam | Blocs de 1 h 30 |
| Capacité du hammam | 10 personnes par plage |
| Soins | 2 salles et 2 masseuses : 2 soins en même temps au maximum |
| Limite par client | 2 soins par visite |

## Choix techniques

- **Prix stockés en cents (entiers)** pour éviter les erreurs d'arrondi des nombres à virgule flottante.
- **Patron « application factory »** (`create_app`) pour créer une application séparée pour les tests.
- **Clé secrète lue depuis une variable d'environnement** pour ne jamais publier de secret dans le code.

## Installation

```bash
git clone https://github.com/Ti-Bayo/hammam-reservations.git
cd hammam-reservations
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
flask --app run init-db
python run.py
```

L'application est ensuite accessible à l'adresse http://127.0.0.1:5000.

## Structure

```
app/
  __init__.py     # création de l'application
  models.py       # modèles Service, Client, Reservation
  donnees.py      # commande init-db et services de départ
  routes.py       # pages
  templates/      # gabarits HTML (Jinja2 + Bootstrap)
tests/
run.py
```

## Auteure

Tiguidanké II Bayo, étudiante en génie informatique à l'Université Laval
[LinkedIn](https://www.linkedin.com/in/tiguidanké-2-bayo)