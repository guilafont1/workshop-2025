# 🧬 Room 4 - Laboratoire d'Analyse Génétique

## Aperçu
La Room 4 a été entièrement redesignée pour s'intégrer parfaitement dans le thème hospitalier du jeu. Elle propose maintenant un puzzle complexe d'analyse génétique où les joueurs doivent reconstituer une séquence ADN virale à partir de dossiers médicaux cryptés.

## Thème médical cohérent
- **Contexte** : Laboratoire de biologie moléculaire en situation d'urgence
- **Mission** : Analyser des échantillons de patients infectés par un virus inconnu
- **Outils** : Microscope électronique, PCR quantitative, base de données GenBank
- **Durée estimée** : 12-18 minutes (plus complexe que les versions précédentes)

## Mécanisme du puzzle

### 1. Dossiers patients infectés
Quatre patients avec des données médicales détaillées :
- **PAT-A001** - Dr. Adams (Patient zéro, virologue)
- **PAT-T002** - Pr. Taylor (Chef infectiologie) 
- **PAT-C003** - Dr. Chen (Interne biologie moléculaire)
- **PAT-G004** - Dr. Garcia (Épidémiologiste)

### 2. Indices cachés multiples
Chaque dossier contient des indices cryptés dans :
- **Identifiants** : PAT-**X**00Y où X = nucléotide
- **Poids moléculaires** : Conversions hexadécimales complexes
- **Heures de prélèvement** : Codes temporels
- **Températures d'échantillon** : Stabilité des liaisons
- **Analyses complètes** : Descriptions détaillées avec indices structurels

### 3. Règles de biologie moléculaire
- **Appariement Watson-Crick** : A↔T et C↔G
- **Liaisons hydrogène** : A-T (2 liaisons), C-G (3 liaisons)  
- **Classification** : Purines (A,G) vs Pyrimidines (T,C)
- **Ordre de position** : Basé sur les indices numériques cachés

## Solution attendue
**Séquence correcte** : `ATCG`

### Logique de résolution
1. **Identification** : Chaque patient correspond à un nucléotide (A, T, C, G)
2. **Positionnement** : Les indices révèlent l'ordre (position 1, 2, 3, 4)
3. **Validation** : Vérification des règles d'appariement génétique
4. **Reconstitution** : Assemblage de la séquence complète

## Complexité accrue

### Indices multicouches
- **Niveau 1** : Identifiants évidents (PAT-A001 → A)
- **Niveau 2** : Données numériques cryptées (poids moléculaires)
- **Niveau 3** : Codes temporels et thermiques
- **Niveau 4** : Analyse structurelle des liaisons hydrogène

### Validation intelligente
- Messages d'erreur progressifs et pédagogiques
- Gestion des formats d'entrée multiples (espaces, tirets)
- Indices adaptatifs selon le type d'erreur
- Support majuscules/minuscules automatique

### Interface immersive
- Design cohérent avec le thème hospitalier
- Cartes patients détaillées avec données médicales réalistes
- Outils de laboratoire avec états (disponible/hors service)
- Référentiel de biologie moléculaire intégré
- Animations et effets visuels thématiques

## Intégration système
- **Fichier principal** : `game/puzzles.py` - Fonctions `room4_get_genetic_data()` et `room4_validate_genetic_sequence()`
- **Template** : `templates/room4.html` - Interface graphique complète avec CSS intégré
- **Routage** : `app.py` - Gestion des données génétiques et validation des séquences

## Accessibilité et expérience utilisateur
- **Responsive design** : Adaptation mobile/tablette
- **Aide contextuelle** : Indices progressifs selon les erreurs
- **Feedback immédiat** : Validation en temps réel avec messages clairs
- **Thème sombre** : Cohérent avec l'ambiance du jeu

Cette nouvelle version de la Room 4 offre une expérience beaucoup plus riche et cohérente, tout en étant significativement plus complexe à résoudre, nécessitant une analyse approfondie des multiples couches d'indices pour reconstituer la séquence génétique complète.