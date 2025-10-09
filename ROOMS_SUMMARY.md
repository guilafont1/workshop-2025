# Résumé des Rooms (1 → 6)

Ce document rassemble en une page la documentation synthétique des six rooms du jeu (Rooms 1 à 6). Il reprend le thème, le mécanisme, la solution attendue, les intégrations techniques et les notes d'interface pour chaque room.

---

## Room 1 — Système de Surveillance Cardiaque
- Thème : Salle de monitoring cardiaque (ambiance rétro-futuriste).
- Mission : Calculer le BPM moyen des patients âgés de 68 à 72 ans.
- Données : 8 patients avec âge et BPM.
- Règles : Filtrer patients 68–72 ans, moyenne arithmétique, arrondir à l'entier.
- Solution attendue : `79` (moyenne de 76, 74, 70, 78, 80, 74 → 78.666... → 79).
- Intégration : fonctions dans `game/puzzles.py` (`room1_get_patients_data()`, `room1_check_bpm()`), template `templates/room1.html`, routage dans `app.py`.

Points UX/validation : surlignage automatique des cibles, tolérance nulle (réponse exacte), indices progressifs et feedback pédagogique.

---

## Room 2 — Prescription Médicamenteuse
- Thème : Pharmacie hospitalière.
- Mission : Prescrire 5 médicaments corrects en tenant compte d'allergies, interactions et contre‑indications.
- Médicaments : Paracétamol, Ibuprofène, Aspirine, Sirop antitussif, Sumatriptan, Complexe vitamine B.
- Règles : Interdire allergènes, éviter interactions (AINS + anticoagulants), respecter grossesse et indications.
- Solution attendue : Alice → Paracétamol; Bob → Paracétamol; Clara → Sirop antitussif; Daniel → Complexe vitamine B; Emma → Paracétamol.
- Intégration : `game/puzzles.py` (`room2_get_prescription_data()`, `room2_validate_prescriptions()`), template `templates/room2.html`, routage dans `app.py`.

Points UX/validation : feedback patient-par-patient, score partiel (X/5), messages pédagogiques et alertes visuelles pour contre‑indications.

---

## Room 3 — Calcul d'Hydratation
- Thème : Service de réanimation, calculs médicaux avancés.
- Mission : Calculer les besoins hydriques pour 4 patients (ajustements selon pathologie).
- Formules clefs : adultes 30–35 ml/kg/j, enfants 50–100 ml/kg/j, +500 ml fièvre, +1000 ml post‑op, -50% insuffisance rénale, +500 ml grossesse.
- Solutions attendues :
  - Gabriel → 3125 ml
  - Hélène → 4200 ml
  - Isaac → 975 ml
  - Julia → 2425 ml
- Intégration : `game/puzzles.py` (`room3_get_hydration_data()`, `room3_validate_hydration()`), template `templates/room3.html`, routage dans `app.py`.

Points UX/validation : tolérance ±10% (réalisme médical), calculateur intégré avec vérification et explications détaillées.

---

## Room 4 — (Référence)
La documentation détaillée de la Room 4 (analyse génétique / séquence virale) se trouve dans `ROOM4_DOCUMENTATION.md`. Elle est liée narrativement entre Room 3 (hydratation) et Rooms 5–6 (laboratoire & patient zéro).

---

## Rooms 5 & 6 — Laboratoire P4 et Chambre d'Isolation (Finales)
- Thème : Confinement biologique / patient zéro — montée en tension avec timers et conséquences dramatiques.

Room 5 — Laboratoire P4 :
- Mission : Trouver un code d'urgence 5 chiffres en analysant 5 équipements.
- Indices : Microscope (6), Analyseur (8), Centrifugeuse (4), Moniteur cryo (6), Système injection (7).
- Solution attendue : `68467`.
- UX : timer 5 minutes, interface immersive, validation progressive, messages d'aide.

Room 6 — Chambre d'Isolation :
- Mission : Corriger 3 segments mutés pour synthétiser l'antidote.
- Segments & corrections : SEGMENT ALPHA → `ATCG`; BETA → `ATGC`; GAMMA → `ATCG`.
- Solution attendue : `ATCG-ATGC-ATCG`.
- UX : timer 7 minutes, patient simulé, validation par segment, feedback détaillé.

Intégration technique : logique côté backend pour validation progressive (`game/puzzles.py`), templates `templates/room5.html` et `templates/room6.html` à créer/compléter, mécaniques JS/CSS pour timers et animations.

---

## Notes d'implémentation communes
- Backend : centraliser la logique de validation dans `game/puzzles.py` et exposer des routes claires dans `app.py`.
- Frontend : templates sous `templates/` + styles dans `static/style.css`. Utiliser JS pour timers, animations et formatage d'inputs.
- Accessibilité : responsive, indices progressifs et explications détaillées en cas d'erreur.

## Fichiers de référence
- `ROOM1_DOCUMENTATION.md`, `ROOM2_DOCUMENTATION.md`, `ROOM3_DOCUMENTATION.md`, `ROOM4_DOCUMENTATION.md`, `ROOMS_5_6_DOCUMENTATION.md`
- Intégration code : `game/puzzles.py`, `app.py`, `templates/*.html`, `static/style.css`.

## Prochaines étapes recommandées
1. Vérifier/compléter `ROOM4_DOCUMENTATION.md` et lier explicitement les endpoints dans `app.py`.
2. Ajouter/mettre à jour les templates `room5.html` et `room6.html` pour respecter les timers et l'immersion.
3. Écrire de petits tests unitaires pour chaque fonction de validation dans `game/puzzles.py` (happy path + 1 cas d'erreur).

---

Résumé : ce fichier regroupe les éléments essentiels des six rooms, les solutions attendues, les points d'intégration et une feuille de route courte pour finaliser l'implémentation et la validation automatisée.
