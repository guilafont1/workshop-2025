# 💊 Room 2 - Prescription Médicamenteuse

## Aperçu
La Room 2 élève la difficulté avec une énigme de pharmacologie médicale. Les joueurs doivent prescrire les médicaments appropriés à chaque patient en tenant compte d'allergies, interactions médicamenteuses et contre-indications, simulant le travail d'un pharmacien hospitalier.

## Thème médical cohérent
- **Contexte** : Pharmacie hospitalière d'urgence
- **Mission** : Prescrire correctement 5 médicaments selon protocoles médicaux
- **Outils** : Base de données médicamenteuse, dossiers patients détaillés
- **Durée estimée** : 12-15 minutes (énigme intermédiaire complexe)

## Mécanisme du puzzle

### 1. Patients nécessitant traitement
Cinq patients avec profils médicaux complexes :
- **Alice** : Fièvre + maux de tête, allergie aspirine
- **Bob** : Douleur articulaire, traitement anticoagulant
- **Clara** : Toux sèche, grossesse
- **Daniel** : Fatigue, ISRS (antidépresseur)
- **Emma** : Migraine sévère, première crise

### 2. Médicaments disponibles
Six options thérapeutiques avec caractéristiques détaillées :
- **Paracétamol** : Fièvre/douleur, pas d'interactions majeures
- **Ibuprofène** : Douleur/inflammation, contre-indiqué grossesse/anticoagulants
- **Aspirine** : Douleur/fièvre, allergie fréquente
- **Sirop antitussif** : Toux, contre-indiqué grossesse
- **Sumatriptan** : Migraine, incompatible ISRS
- **Complexe vitaminé B** : Fatigue, compatible général

### 3. Règles pharmacologiques strictes
- **Allergies** : Interdiction totale des substances allergènes
- **Interactions** : Éviter combinaisons dangereuses (AINS + anticoagulants)
- **Grossesse** : Contre-indications spécifiques
- **Indications** : Respect des symptômes cibles

## Solution attendue
**Prescriptions correctes** :
- Alice → Paracétamol
- Bob → Paracétamol
- Clara → Sirop antitussif
- Daniel → Complexe vitaminé B
- Emma → Paracétamol

### Logique de résolution
1. **Analyse patient** : Identifier symptômes, allergies, traitements
2. **Filtrage médicaments** : Éliminer contre-indications et interactions
3. **Sélection optimale** : Choisir le plus adapté aux symptômes
4. **Validation globale** : Vérifier cohérence de l'ensemble

## Complexité accrue

### Indices multicouches
- **Niveau 1** : Symptômes et allergies évidents
- **Niveau 2** : Traitements actuels et interactions
- **Niveau 3** : Connaissances pharmacologiques générales
- **Niveau 4** : Raisonnement déductif sur combinaisons

### Validation intelligente
- Feedback détaillé par patient avec explication médicale
- Score partiel affiché (X/5 correct)
- Messages pédagogiques sur erreurs pharmacologiques
- Indices adaptatifs selon type de faute

### Interface professionnelle
- Design de logiciel médical hospitalier
- Dropdowns de prescription sécurisés
- Alertes visuelles pour contre-indications
- Base de données médicamenteuse intégrée

## Intégration système
- **Fichier principal** : [`game/puzzles.py`](game/puzzles.py ) - Fonctions `room2_get_prescription_data()` et `room2_validate_prescriptions()`
- **Template** : [`templates/room2.html`](templates/room2.html ) - Interface prescription avec CSS intégré
- **Routage** : [`app.py`](app.py ) - Gestion des données pharmacologiques et validation

## Accessibilité et expérience utilisateur
- **Responsive design** : Adaptation mobile avec formulaires adaptés
- **Aide contextuelle** : Rappels des règles pharmacologiques
- **Feedback détaillé** : Explications médicales des erreurs
- **Thème médical** : Interface professionnelle d'hôpital

Cette Room 2 offre une expérience authentique de prescription médicale, nécessitant une analyse approfondie des interactions médicamenteuses et contre-indications pour réussir.