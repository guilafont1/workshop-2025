# 💧 Room 3 - Calcul d'Hydratation

## Aperçu
La Room 3 clôt le premier tiers du jeu avec un puzzle de calcul médical avancé. Les joueurs doivent calculer précisément les besoins en hydratation de patients hospitalisés selon leur âge, poids, pathologie et traitement, simulant les compétences d'un infirmier en réanimation.

## Thème médical cohérent
- **Contexte** : Service de réanimation hospitalière
- **Mission** : Calculer l'hydratation optimale pour 4 patients
- **Outils** : Formules médicales, données patient, calculateur intégré
- **Durée estimée** : 15-20 minutes (énigme calculatoire complexe)

## Mécanisme du puzzle

### 1. Patients nécessitant hydratation
Quatre profils médicaux variés :
- **Gabriel** : 45 ans, 75kg, pneumonie, fièvre 39°C
- **Hélène** : 12 ans, 40kg, appendicite, post-opératoire
- **Isaac** : 78 ans, 65kg, insuffisance rénale, dialyse
- **Julia** : 32 ans, 55kg, grossesse, pré-éclampsie

### 2. Formules d'hydratation médicales
Calculs basés sur protocoles hospitaliers :
- **Formule adulte** : 30-35 ml/kg/jour selon pathologie
- **Formule enfant** : 50-100 ml/kg/jour selon âge
- **Ajustements** : +500ml fièvre, +1000ml post-opératoire
- **Réduction** : -50% insuffisance rénale, +500ml grossesse

### 3. Interface de calcul
Calculateur intégré avec :
- **Saisie manuelle** : Entrée des calculs personnels
- **Vérification automatique** : Validation des résultats
- **Tolérance médicale** : ±10% acceptable pour réalisme
- **Feedback détaillé** : Explication des écarts

## Solution attendue
**Calculs corrects** :
- Gabriel (45ans, 75kg, pneumonie + fièvre) → 75kg × 35ml + 500ml = **3125ml**
- Hélène (12ans, 40kg, appendicite post-op) → 40kg × 80ml + 1000ml = **4200ml**
- Isaac (78ans, 65kg, insuffisance rénale) → 65kg × 30ml × 0.5 = **975ml**
- Julia (32ans, 55kg, grossesse pré-éclampsie) → 55kg × 35ml + 500ml = **2425ml**

### Logique de résolution
1. **Analyse patient** : Âge, poids, pathologie, facteurs spéciaux
2. **Application formule** : Base selon âge + ajustements pathologiques
3. **Calcul précis** : Multiplication et additions correctes
4. **Validation tolérante** : Acceptation ±10% pour réalisme médical

## Complexité mathématique

### Niveaux de difficulté
- **Calcul 1** : Formule simple adulte (Gabriel)
- **Calcul 2** : Ajustement pathologique (Hélène)
- **Calcul 3** : Réduction rénale (Isaac)
- **Calcul 4** : Combinaison grossesse (Julia)

### Validation pédagogique
- **Tolérance ±10%** : Réalisme médical (erreurs de calcul acceptables)
- **Feedback détaillé** : Explication des écarts et corrections
- **Score progressif** : Validation patient par patient
- **Indices mathématiques** : Rappels des formules médicales

### Interface calculatoire
- **Calculateur intégré** : Boutons numériques et opérations
- **Affichage patient** : Données médicales claires
- **Validation temps réel** : Feedback immédiat des calculs
- **Thème médical** : Interface de service hospitalier

## Intégration système
- **Fichier principal** : [`game/puzzles.py`](game/puzzles.py ) - Fonctions `room3_get_hydration_data()` et `room3_validate_hydration()`
- **Template** : [`templates/room3.html`](templates/room3.html ) - Interface calculatrice avec CSS intégré
- **Routage** : [`app.py`](app.py ) - Gestion des données d'hydratation et validation

## Accessibilité et expérience utilisateur
- **Calculateur visuel** : Interface intuitive avec boutons
- **Aide contextuelle** : Rappels des formules médicales
- **Feedback détaillé** : Explications des erreurs de calcul
- **Responsive design** : Adaptation mobile avec calculateur adapté

Cette Room 3 offre une expérience authentique de calcul médical hospitalier, nécessitant précision mathématique et connaissance des protocoles d'hydratation pour réussir.