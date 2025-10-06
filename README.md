# Virus.Life — Hôpital sous attaque (100% Python)

Projet d'Escape Game éducatif en **Flask** (Python pur, sans framework JS côté client).
Collaboration possible par plusieurs joueurs en simultané (mode "coop" via état serveur + rechargements).

## Lancer en local
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export FLASK_APP=app.py  # Windows: set FLASK_APP=app.py
python app.py
```
Le jeu sera disponible sur http://127.0.0.1:5000

## Structure
```
VirusLife/
  app.py
  game/
    puzzles.py
    state.py
    utils.py
  templates/
    base.html
    index.html
    lobby.html
    room1.html
    room2.html
    room3.html
    room4.html
    room5.html
    success.html
    fail.html
  static/
    style.css
  data/
    logs.txt
    patients_corrupted.json
    virus_code.py
    secret_message.fernet
  db/
    game_state.json
```

## Thèmes pédagogiques
- Encodage, hachage, chiffrement (salle 1 & 3)
- Nettoyage et validation de données (salle 2)
- Coordination réseau (salle 4)
- Culture cyber & gestion du stress (salle 5)
