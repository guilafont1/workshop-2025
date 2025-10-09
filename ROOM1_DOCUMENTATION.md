# 🫀 Room 1 - Système de Surveillance Cardiaque

## Aperçu
La Room 1 initie le jeu avec un puzzle de calcul médical simple mais immersif. Les joueurs doivent analyser les données de surveillance cardiaque de patients hospitalisés pour déterminer le rythme cardiaque moyen d'une tranche d'âge spécifique.

## Thème médical cohérent
- **Contexte** : Salle de surveillance intensive avec moniteurs cardiaques
- **Mission** : Calculer le BPM moyen des patients âgés de 68-72 ans
- **Outils** : Données patients en temps réel, calculateur intégré
- **Durée estimée** : 5-8 minutes (énigme d'introduction)

## Mécanisme du puzzle

### 1. Données patients hospitalisés
Huit patients avec profils médicaux détaillés :
- **Alice Dupont** (65 ans) - 72 BPM
- **Bob Martin** (70 ans) - 76 BPM
- **Clara Bernard** (68 ans) - 74 BPM
- **Daniel Petit** (72 ans) - 70 BPM
- **Emma Moreau** (69 ans) - 78 BPM
- **François Roux** (71 ans) - 80 BPM
- **Gabrielle Leroy** (67 ans) - 74 BPM
- **Henri Simon** (73 ans) - 71 BPM

### 2. Indices intégrés
Chaque patient inclut :
- **Âge** : Critère de sélection (68-72 ans)
- **BPM** : Valeurs individuelles à moyenner
- **Commentaires** : Indices contextuels médicaux
- **Surlignage automatique** : Mise en évidence des patients cibles après 4 secondes

### 3. Règles mathématiques médicales
- **Sélection** : Patients dans la plage d'âge 68-72 ans uniquement
- **Calcul** : Moyenne arithmétique des BPM sélectionnés
- **Précision** : Arrondi à l'entier le plus proche
- **Validation** : Tolérance nulle (réponse exacte requise)

## Solution attendue
**BPM moyen** : `79`

### Logique de résolution
1. **Filtrage** : Identifier les 6 patients âgés de 68-72 ans
2. **Extraction** : Collecter leurs BPM (76, 74, 70, 78, 80, 74)
3. **Calcul** : (76+74+70+78+80+74)/6 = 78.666... → 79
4. **Saisie** : Entrer la valeur exacte dans le formulaire

## Complexité équilibrée

### Indices progressifs
- **Niveau 1** : Tableau avec âges et BPM visibles
- **Niveau 2** : Surlignage automatique des patients cibles
- **Niveau 3** : Commentaires médicaux contextuels
- **Niveau 4** : Calculateur intégré avec étapes guidées

### Validation pédagogique
- Messages d'erreur avec calcul correct affiché
- Explications mathématiques détaillées
- Indices supplémentaires en cas d'échec répété
- Support pour formats numériques multiples

### Interface rétro-futuriste
- Design d'ordinateur vintage des années 80
- Écran CRT avec effets de scanlines
- Animations de boot système immersives
- Thème vert monochrome médical

## Intégration système
- **Fichier principal** : [`game/puzzles.py`](game/puzzles.py ) - Fonctions `room1_get_patients_data()` et `room1_check_bpm()`
- **Template** : [`templates/room1.html`](templates/room1.html ) - Interface surveillance avec CSS intégré
- **Routage** : [`app.py`](app.py ) - Gestion des données BPM et validation

## Accessibilité et expérience utilisateur
- **Responsive design** : Adaptation mobile/tablette avec cartes patients
- **Aide contextuelle** : Indices mathématiques intégrés
- **Feedback immédiat** : Validation avec explication détaillée
- **Thème sombre** : Cohérent avec l'ambiance hospitalière nocturne

Cette Room 1 constitue une introduction parfaite au jeu, combinant calculs mathématiques simples avec une immersion médicale réaliste et des indices pédagogiques progressifs.