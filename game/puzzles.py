from typing import Dict, Any, List, Tuple
import json, os, time
from game.utils import sha256_hex, b64_decode
from cryptography.fernet import Fernet

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

# --------- ROOM 1: TROUVE LE RYTHME DU CŒUR 🫀 ---------
# Calculer le rythme cardiaque moyen des patients de 68-72 ans
def room1_get_patients_data() -> Dict[str, Any]:
    """Retourne les données des patients pour l'épreuve BPM"""
    return {
        "patients": [
            {"nom": "Alice", "age": 68, "bpm": 72, "commentaire": "Patient stable depuis ce matin. A pris ses médicaments à 8h comme d'habitude. Tension artérielle normale (12/8). Toujours calme et coopérative. Aucune plainte particulière. Sommeil réparateur cette nuit."},
            {"nom": "Bob", "age": 70, "bpm": 76, "commentaire": "Excellent moral aujourd'hui ! A bien mangé au petit-déjeuner. Glycémie stable à 1.2g/L. Toujours souriant avec le personnel soignant. A fait quelques pas dans le couloir ce matin. Famille venue hier soir."},
            {"nom": "Clara", "age": 71, "bpm": 74, "commentaire": "Respiration un peu courte après effort. A besoin de pauses fréquentes pour les activités. Oxygénation correcte au repos (98%). Se fatigue vite mais garde le moral. Kinésithérapie programmée cet après-midi."},
            {"nom": "Daniel", "age": 69, "bpm": 70, "commentaire": "Nuit agitée, s'est endormi tard vers 23h30. Traitement pour l'insomnie ajusté. Endormi souvent dans la journée, probablement rattrapant le sommeil. Pas de fièvre. Constantes stables malgré la fatigue."},
            {"nom": "Emma", "age": 70, "bpm": 78, "commentaire": "Très dynamique ce matin ! A participé à toutes les activités de rééducation. Appétit excellent, a terminé tous ses repas. Toujours active et motivée pour les soins. Demande à sortir se promener dans le jardin."},
            {"nom": "Félix", "age": 72, "bpm": 80, "commentaire": "Patient agité, ne tient pas en place. A déjà fait 3 tours du service ce matin. Hyperactif comme d'habitude. Bouge beaucoup les mains quand il parle. Attention aux chutes, surveillance renforcée demandée."},
            {"nom": "Gérard", "age": 70, "bpm": 74, "commentaire": "Humeur excellente aujourd'hui ! Raconte des blagues au personnel. Patient joyeux qui remonte le moral de ses voisins de chambre. A bien dormi. Visite de sa petite-fille prévue cet après-midi."},
            {"nom": "Hannah", "age": 69, "bpm": 71, "commentaire": "Patiente très zen aujourd'hui. Méditation matinale effectuée avec succès. Calme et souriante avec tout le monde. Tension artérielle parfaite. Pratique ses exercices de respiration régulièrement."}
        ],
        "age_range": (68, 72),
        "correct_answer": 74,  # Moyenne des BPM des patients 68-72 ans
        "calculation": "Patients 68-72 ans: 72+76+74+70+78+80+74+71 = 595, 595/8 = 74 bpm"
    }

def room1_check_bpm(user_bpm: int) -> bool:
    """Valide si le BPM calculé est correct"""
    data = room1_get_patients_data()
    return user_bpm == data["correct_answer"]

# --------- ROOM 2: LE BON MÉDICAMENT 💊 ---------
# Puzzle complexe avec interactions médicamenteuses et contraintes
def room2_get_prescription_data() -> Dict[str, Any]:
    """Retourne les données pour l'épreuve des médicaments complexe"""
    return {
        "patients": [
            {
                "nom": "Alice", 
                "age": 45,
                "symptomes": ["Fièvre 38.5°C", "Maux de tête", "Fatigue"],
                "allergies": ["Aspirine"],
                "traitements_actuels": ["Vitamine D"],
                "historique": "Hypertension contrôlée depuis 2 ans"
            },
            {
                "nom": "Bob", 
                "age": 67,
                "symptomes": ["Douleur articulaire genou", "Raideur matinale"],
                "allergies": ["Aucune"],
                "traitements_actuels": ["Anticoagulant (Warfarine)"],
                "historique": "Risque hémorragique élevé"
            },
            {
                "nom": "Clara", 
                "age": 32,
                "symptomes": ["Toux sèche persistante", "Gorge irritée"],
                "allergies": ["Codéine"],
                "traitements_actuels": ["Pilule contraceptive"],
                "historique": "Enceinte de 6 semaines (découvert ce matin)"
            },
            {
                "nom": "Daniel", 
                "age": 29,
                "symptomes": ["Fatigue extrême", "Difficultés concentration"],
                "allergies": ["Pénicilline"],
                "traitements_actuels": ["Antidépresseur (Sertraline)"],
                "historique": "Dépression en cours de traitement"
            },
            {
                "nom": "Emma", 
                "age": 55,
                "symptomes": ["Migraine sévère", "Nausées", "Photophobie"],
                "allergies": ["Aucune"],
                "traitements_actuels": ["Aucun"],
                "historique": "Première crise de migraine"
            }
        ],
        "medicaments_disponibles": [
            {
                "nom": "Paracétamol",
                "indications": ["Fièvre", "Douleur légère", "Maux de tête"],
                "contre_indications": ["Insuffisance hépatique sévère"],
                "interactions": [],
                "grossesse": "Autorisé"
            },
            {
                "nom": "Ibuprofène", 
                "indications": ["Douleur", "Inflammation", "Fièvre"],
                "contre_indications": ["Anticoagulants", "Grossesse 3e trimestre"],
                "interactions": ["Anticoagulant"],
                "grossesse": "Éviter"
            },
            {
                "nom": "Aspirine",
                "indications": ["Douleur", "Fièvre", "Anti-agrégant"],
                "contre_indications": ["Allergie", "Anticoagulants", "Enfants"],
                "interactions": ["Anticoagulant"],
                "grossesse": "Contre-indiqué"
            },
            {
                "nom": "Sirop antitussif",
                "indications": ["Toux sèche"],
                "contre_indications": ["Allergie codéine"],
                "interactions": [],
                "grossesse": "Autorisé avec précaution"
            },
            {
                "nom": "Complexe vitaminé B",
                "indications": ["Fatigue", "Stress", "Dépression"],
                "contre_indications": [],
                "interactions": [],
                "grossesse": "Autorisé"
            },
            {
                "nom": "Sumatriptan",
                "indications": ["Migraine sévère"],
                "contre_indications": ["Hypertension", "Grossesse"],
                "interactions": ["Antidépresseurs ISRS"],
                "grossesse": "Contre-indiqué"
            }
        ],
        "indices": [
            "⚠️ Vérifiez TOUJOURS les allergies avant de prescrire",
            "💊 Les anticoagulants (Warfarine) sont incompatibles avec Aspirine et Ibuprofène",
            "🤰 Clara est enceinte : évitez les médicaments contre-indiqués",
            "🧠 Les antidépresseurs ISRS (Sertraline) interagissent avec le Sumatriptan",
            "💡 Le Paracétamol est souvent le choix le plus sûr pour la fièvre",
            "🔍 Parfois, plusieurs médicaments peuvent traiter le même symptôme"
        ],
        "solution": {
            "Alice": "Paracétamol",        # Fièvre + maux de tête, éviter Aspirine (allergie)
            "Bob": "Paracétamol",          # Douleur, éviter AINS (anticoagulant)
            "Clara": "Sirop antitussif",   # Toux, enceinte donc attention aux contre-indications
            "Daniel": "Complexe vitaminé B", # Fatigue, éviter Sumatriptan (interaction ISRS)
            "Emma": "Paracétamol"          # Migraine, éviter Sumatriptan (première crise)
        },
        "explanations": {
            "Alice": "Paracétamol pour la fièvre (allergie à l'Aspirine)",
            "Bob": "Paracétamol car les AINS sont contre-indiqués avec les anticoagulants",
            "Clara": "Sirop antitussif compatible grossesse (pas de codéine)",
            "Daniel": "Vitamines B pour la fatigue (Sumatriptan interagit avec antidépresseurs)",
            "Emma": "Paracétamol pour débuter (éviter Sumatriptan en première intention)"
        }
    }

def room2_validate_prescriptions(prescriptions: Dict[str, str]) -> Tuple[bool, str]:
    """Valide les prescriptions des médicaments avec logique complexe"""
    data = room2_get_prescription_data()
    solution = data["solution"]
    explanations = data["explanations"]
    
    errors = []
    
    for patient_name, prescribed_med in prescriptions.items():
        if patient_name not in solution:
            return False, f"Patient {patient_name} inconnu"
        
        # Trouver les données du patient
        patient = next(p for p in data["patients"] if p["nom"] == patient_name)
        
        # Trouver les infos du médicament prescrit
        med_info = next((m for m in data["medicaments_disponibles"] if m["nom"] == prescribed_med), None)
        if not med_info:
            errors.append(f"{patient_name}: Médicament '{prescribed_med}' non disponible")
            continue
        
        # Vérifier les allergies
        if prescribed_med in [allergy for allergy in patient["allergies"]]:
            errors.append(f"{patient_name}: Allergie à {prescribed_med} !")
            continue
        
        # Vérifier les interactions avec traitements actuels
        for traitement in patient["traitements_actuels"]:
            if "Anticoagulant" in traitement and prescribed_med in ["Aspirine", "Ibuprofène"]:
                errors.append(f"{patient_name}: {prescribed_med} interagit avec {traitement}")
                continue
            if "Sertraline" in traitement and prescribed_med == "Sumatriptan":
                errors.append(f"{patient_name}: Interaction dangereuse Sumatriptan + antidépresseur")
                continue
        
        # Vérifier grossesse pour Clara
        if patient_name == "Clara" and prescribed_med in ["Ibuprofène", "Aspirine", "Sumatriptan"]:
            errors.append(f"{patient_name}: {prescribed_med} contre-indiqué pendant la grossesse")
            continue
        
        # Vérifier si le médicament traite les symptômes
        patient_symptoms_keywords = " ".join(patient["symptomes"]).lower()
        med_indications = " ".join(med_info["indications"]).lower()
        
        symptom_match = False
        if "fièvre" in patient_symptoms_keywords and any(x in med_indications for x in ["fièvre", "douleur"]):
            symptom_match = True
        elif "douleur" in patient_symptoms_keywords and "douleur" in med_indications:
            symptom_match = True
        elif "toux" in patient_symptoms_keywords and "toux" in med_indications:
            symptom_match = True
        elif "fatigue" in patient_symptoms_keywords and any(x in med_indications for x in ["fatigue", "stress"]):
            symptom_match = True
        elif "migraine" in patient_symptoms_keywords and any(x in med_indications for x in ["migraine", "douleur"]):
            symptom_match = True
        elif "maux de tête" in patient_symptoms_keywords and any(x in med_indications for x in ["douleur", "maux"]):
            symptom_match = True
        
        if not symptom_match:
            errors.append(f"{patient_name}: {prescribed_med} ne traite pas les symptômes présents")
    
    if errors:
        return False, "Erreurs détectées:\n• " + "\n• ".join(errors[:3])  # Limite à 3 erreurs pour lisibilité
    
    # Vérifier si c'est exactement la solution optimale
    correct_count = sum(1 for name, med in prescriptions.items() if med == solution.get(name))
    total = len(solution)
    
    if correct_count == total:
        return True, "🎉 Prescriptions parfaites ! Tous les patients sont traités de manière optimale."
    elif correct_count >= total * 0.8:  # 80% de bonnes réponses
        return True, f"✅ Prescriptions acceptables ({correct_count}/{total} optimales). Patients traités en sécurité."
    else:
        return False, f"Prescriptions sous-optimales ({correct_count}/{total}). Révisez les contre-indications et interactions."
    
# --------- ROOM 3: HYDRATATION ET TEMPÉRATURE 🌡️💧 ---------
# Puzzle complexe avec calculs, graphiques et monitoring patients
def room3_get_hydration_data() -> Dict[str, Any]:
    """Retourne les données pour l'épreuve hydratation/température complexe"""
    patients_data = [
        {
            "nom": "Alice",
            "age": 34,
            "poids": 65,
            "temperature": 38.8,
            "facteur_fievre": 950,  # (38.8-37) * 500 = 950ml
            "pathologie": "Grippe saisonnière",
            "hydratation_actuelle": 1.2
        },
        {
            "nom": "Bob",
            "age": 72,
            "poids": 78,
            "temperature": 39.4,
            "facteur_fievre": 1200,  # (39.4-37) * 500 = 1200ml
            "pathologie": "Insuffisance cardiaque",
            "hydratation_actuelle": 0.9
        },
        {
            "nom": "Clara",
            "age": 28,
            "poids": 58,
            "temperature": 37.1,
            "facteur_fievre": 0,  # Température normale
            "pathologie": "Diabète",
            "hydratation_actuelle": 2.2
        },
        {
            "nom": "Daniel",
            "age": 45,
            "poids": 85,
            "temperature": 40.1,
            "facteur_fievre": 1550,  # (40.1-37) * 500 = 1550ml
            "pathologie": "Infection",
            "hydratation_actuelle": 1.1
        },
        {
            "nom": "Emma",
            "age": 19,
            "poids": 52,
            "temperature": 36.7,
            "facteur_fievre": 0,  # Température normale
            "pathologie": "Diabète",
            "hydratation_actuelle": 1.8
        }
    ]

    return {
        "patients": patients_data,
        "options_calcul": [1.0, 1.5, 2.0, 2.5, 2.8, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0],
        "règles": {
            "36.1-37.2°C": "Température normale, hydratation standard",
            "37.3-38.0°C": "Température légèrement élevée",
            "38.1-39.0°C": "Fièvre modérée, augmenter l'hydratation",
            "39.1-40.0°C": "Forte fièvre, hydratation intensive requise"
        }
    }

def room3_validate_hydration(hydration_choices: Dict[str, float]) -> Tuple[bool, str]:
    """Valide les choix d'hydratation avec calculs médicaux"""
    # Solutions attendues basées sur les calculs médicaux
    solutions = {
        "Alice": 2.8,    # 65kg × 30ml = 1950ml + fièvre (950ml) = 2900ml ≈ 2.9L, ajusté à 2.8L
        "Bob": 4.5,      # 78kg × 30ml = 2340ml + fièvre (1200ml) + âge (-10%) + insuffisance cardiaque (-20%) ≈ 4.5L
        "Clara": 2.8,    # 58kg × 30ml = 1740ml + diabète (+10%) = 1914ml ≈ 1.9L, mais ajusté pour diabète
        "Daniel": 6.5,   # 85kg × 30ml = 2550ml + fièvre (1550ml) + infection (+15%) ≈ 6.5L
        "Emma": 2.5       # 52kg × 30ml = 1560ml + diabète (+10%) ≈ 1.7L, ajusté
    }

    correct_count = 0
    total_patients = len(solutions)
    tolerance = 0.3  # Tolérance de ±0.3L

    results = []

    for patient_name, prescribed_hydration in hydration_choices.items():
        if patient_name not in solutions:
            return False, f"Patient {patient_name} inconnu"

        expected_hydration = solutions[patient_name]

        if abs(prescribed_hydration - expected_hydration) <= tolerance:
            correct_count += 1
            results.append(f"✅ {patient_name}: {prescribed_hydration}L correct")
        else:
            results.append(f"❌ {patient_name}: {prescribed_hydration}L (attendu: {expected_hydration}L)")

    success_rate = correct_count / total_patients

    if success_rate == 1.0:
        return True, "🎉 Parfait ! Tous les patients sont correctement hydratés."
    elif success_rate >= 0.8:
        return True, f"✅ Prescriptions acceptables ({correct_count}/{total_patients} correctes)."
    else:
        return False, f"Calculs insuffisants ({correct_count}/{total_patients}). Utilisez la calculatrice médicale."
    
def room3_get_calculation_hints() -> Dict[str, str]:
    """Retourne les indices de calcul détaillés"""
    return {
        "etape1": "1️⃣ Calculer besoins de base: Poids × 30-35 mL/kg",
        "etape2": "2️⃣ Ajouter supplément fièvre: (Temp-37°C) × 500mL",
        "etape3": "3️⃣ Correction âge: +15% si >65 ans",
        "etape4": "4️⃣ Correction pathologie: Diabète insipide +60%, Sepsis +50%",
        "etape5": "5️⃣ Vérifier avec diurèse: Normal = 1500-2000mL/24h"
    }

# --------- ROOM 4: ANALYSE GÉNÉTIQUE ET MUTATIONS VIRALES 🧬 ---------
# Puzzle complexe d'analyse de séquences génétiques avec indices cachés
def room4_get_genetic_data() -> Dict[str, Any]:
    """Retourne les données pour l'épreuve d'analyse génétique du virus"""
    return {
        "patients_infectes": [
            {
                "identifiant": "PAT-A001",
                "nom": "Dr. Adams, Sarah",
                "age": 34,
                "fonction": "Virologue senior",
                "statut": "Patient zéro - Premier cas confirmé",
                "sequence_partielle": "ADENINE_START",
                "poids_moleculaire": 331.22,  # Indice : 331 -> 3 (position dans séquence), 31 -> inverse = 13, 1->A, 3->C
                "temperature_echantillon": 4.0,  # Conservation à 4°C
                "taux_mutation": 0.12,
                "localisation": "Laboratoire P4 - Secteur A",
                "heure_prelevement": "08:31",  # Indice caché : 8->H, 31->CF en hexadécimal
                "analyse_complete": "Fragment viral détecté dans échantillon sanguin. Séquence partielle : A---. Liaison hydrogène stable. Complémentarité avec Thymine confirmée. Structure purine avec cycle double. Patient présente symptômes neurologiques aigus.",
                "indices_caches": {
                    "nucleotide": "A",
                    "position_finale": 1,  # Premier nucléotide
                    "complement": "T",
                    "structure": "Purine (double cycle)",
                    "liaisons_h": 2
                }
            },
            {
                "identifiant": "PAT-T002", 
                "nom": "Pr. Taylor, Michael",
                "age": 67,
                "fonction": "Chef du département d'infectiologie",
                "statut": "Contamination secondaire - Contact direct patient zéro",
                "sequence_partielle": "THYMINE_BLOCK",
                "poids_moleculaire": 322.20,  # Indice : 3->C, 22->V, 2->B, 20->T
                "temperature_echantillon": 37.0,  # Température corporelle normale
                "taux_mutation": 0.24,
                "localisation": "Service infectiologie - Chambre 237",
                "heure_prelevement": "14:37",  # Indice : 14->E, 37->% en ASCII proche
                "analyse_complete": "Mutation virale confirmée. Séquence fragmentée : -T--. Structure pyrimidine avec cycle simple identifiée. Appariement avec Adénine vérifié. Patient sous ventilation assistée. Réplication virale active dans les cellules pulmonaires. Pronostic réservé.",
                "indices_caches": {
                    "nucleotide": "T", 
                    "position_finale": 2,  # Deuxième nucléotide
                    "complement": "A",
                    "structure": "Pyrimidine (cycle simple)",
                    "liaisons_h": 2
                }
            },
            {
                "identifiant": "PAT-C003",
                "nom": "Dr. Chen, Wei-Lin", 
                "age": 29,
                "fonction": "Interne en biologie moléculaire",
                "statut": "Exposition accidentelle - Manipulation échantillon",
                "sequence_partielle": "CYTOSINE_FRAG",
                "poids_moleculaire": 305.18,  # Indice complexe : 305->C0E en hex, 18->12 en hex
                "temperature_echantillon": -80.0,  # Congélation ultra-basse
                "taux_mutation": 0.18,
                "localisation": "Laboratoire génomique - Niveau B3",
                "heure_prelevement": "22:18",  # Indice : 22->V, 18->S
                "analyse_complete": "Séquence virale partiellement dégradée : --C-. Structure pyrimidine modifiée détectée. Triple liaison hydrogène avec Guanine confirmée. Stabilité thermique élevée observée. Patient asymptomatique mais porteur. Charge virale faible mais détectable. Surveillance quotidienne nécessaire.",
                "indices_caches": {
                    "nucleotide": "C",
                    "position_finale": 3,  # Troisième nucléotide  
                    "complement": "G",
                    "structure": "Pyrimidine (amino-groupe)",
                    "liaisons_h": 3
                }
            },
            {
                "identifiant": "PAT-G004",
                "nom": "Dr. Garcia, Elena",
                "age": 42, 
                "fonction": "Épidémiologiste",
                "statut": "Contamination nosocomiale - Transmission aéroportée",
                "sequence_partielle": "GUANINE_END",
                "poids_moleculaire": 347.22,  # Indice : 347->14B en hex, 22->16 en hex
                "temperature_echantillon": 25.0,  # Température ambiante
                "taux_mutation": 0.31,
                "localisation": "Bureau épidémiologie - Aile ouest",
                "heure_prelevement": "16:47",  # Indice : 16->G, 47->/ proche en ASCII
                "analyse_complete": "Séquence complète en cours : ---G. Structure purine avec groupe amino identifiée. Complémentarité parfaite avec Cytosine vérifiée. Triple liaison hydrogène stable. Patient présente fièvre intermittente et céphalées. Traitement antiviral prophylactique initié. Évolution favorable attendue.",
                "indices_caches": {
                    "nucleotide": "G",
                    "position_finale": 4,  # Quatrième nucléotide
                    "complement": "C", 
                    "structure": "Purine (groupe amino)",
                    "liaisons_h": 3
                }
            }
        ],
        "outils_analyse": {
            "microscope_electronique": {
                "resolution": "0.1 nanomètre",
                "utilisation": "Visualisation structure moléculaire",
                "disponible": True
            },
            "sequenceur_adn": {
                "precision": "99.9%",
                "vitesse": "2 Mb/h", 
                "utilisation": "Séquençage complet génome viral",
                "disponible": False,
                "erreur": "ERREUR SYSTÈME : Corruption des données de référence"
            },
            "pcr_quantitative": {
                "sensibilite": "1 copie/μL",
                "utilisation": "Amplification et quantification séquences",
                "disponible": True
            },
            "base_donnees_genbank": {
                "acces": "Limité - Connexion instable",
                "sequences_reference": "Partiellement corrompues",
                "disponible": False
            }
        },
        "indices_laboratoire": [
            "🧬 La séquence virale complète est codée dans l'ordre des identifiants patients",
            "🔬 Les poids moléculaires contiennent des indices cachés en conversion hexadécimale", 
            "⏰ Les heures de prélèvement révèlent l'ordre de priorité d'analyse",
            "🌡️ Les températures d'échantillon indiquent la stabilité des liaisons",
            "👥 L'ordre d'infection suit la propagation naturelle du virus : A→T puis C→G",
            "🧪 Les complémentarités Watson-Crick sont la clé : A-T (2 liaisons) et C-G (3 liaisons)",
            "💡 La position finale de chaque nucléotide est cachée dans les données patients"
        ],
        "regles_genetiques": {
            "appariement_watson_crick": {
                "A": "T", "T": "A", "C": "G", "G": "C"
            },
            "liaisons_hydrogene": {
                "A-T": 2, "T-A": 2, "C-G": 3, "G-C": 3
            },
            "classification": {
                "purines": ["A", "G"],  # Double cycle
                "pyrimidines": ["T", "C"]  # Simple cycle
            }
        },
        "sequence_complete_attendue": "ATCG",
        "explication_solution": {
            "methode": "Analyse des indices croisés dans les dossiers patients",
            "etapes": [
                "1. Identifier le nucléotide de chaque patient (A, T, C, G)",
                "2. Extraire la position finale des indices cachés", 
                "3. Ordonner selon position : PAT-A001(pos=1), PAT-T002(pos=2), PAT-C003(pos=3), PAT-G004(pos=4)",
                "4. Construire la séquence : A-T-C-G",
                "5. Vérifier les complémentarités Watson-Crick"
            ]
        }
    }

def room4_validate_genetic_sequence(sequence_input: str) -> Tuple[bool, str]:
    """Valide la séquence génétique reconstituée avec analyse détaillée"""
    data = room4_get_genetic_data()
    expected_sequence = data["sequence_complete_attendue"]
    
    # Nettoyer et normaliser l'input
    cleaned_sequence = sequence_input.strip().upper().replace(" ", "").replace("-", "")
    
    # Vérification de base
    if not cleaned_sequence:
        return False, "⚠️ Erreur : Séquence vide. Veuillez entrer une séquence de nucléotides."
    
    if len(cleaned_sequence) != 4:
        return False, f"⚠️ Erreur : Séquence de longueur incorrecte ({len(cleaned_sequence)}). La séquence virale complète doit contenir exactement 4 nucléotides."
    
    # Vérifier que seuls A, T, C, G sont utilisés
    valid_nucleotides = set("ATCG")
    invalid_chars = set(cleaned_sequence) - valid_nucleotides
    if invalid_chars:
        return False, f"⚠️ Erreur : Caractères invalides détectés : {', '.join(invalid_chars)}. Utilisez uniquement A, T, C, G."
    
    # Vérifier la séquence complète
    if cleaned_sequence == expected_sequence:
        return True, "🎉 SÉQUENCE VIRALE IDENTIFIÉE ! Le génome complet du virus a été reconstitué : ATCG. Propagation virale simulée avec succès. Accès au laboratoire de niveau 5 autorisé. Tous les patients peuvent maintenant être traités efficacement."
    
    # Messages d'aide progressifs selon l'erreur
    correct_positions = sum(1 for i, nucleotide in enumerate(cleaned_sequence) if i < len(expected_sequence) and nucleotide == expected_sequence[i])
    
    if cleaned_sequence == expected_sequence[::-1]:  # Séquence inversée
        return False, "⚠️ Séquence inversée détectée. Les nucléotides sont corrects mais dans l'ordre inverse. Réanalysez les indices de position dans les dossiers patients (PAT-A001, PAT-T002, etc.)."
    
    if set(cleaned_sequence) == set(expected_sequence):  # Bonnes lettres, mauvais ordre
        return False, f"⚠️ Nucléotides corrects mais séquence désordonnée ({correct_positions}/4 positions correctes). Examinez attentivement les indices cachés : poids moléculaires, heures de prélèvement, et identifiants patients."
    
    # Suggestions selon les erreurs communes
    if "CGTA" in cleaned_sequence:
        return False, "⚠️ Séquence proche mais incorrecte. Vérifiez l'ordre d'infection et la propagation virale naturelle. Les purines (A,G) et pyrimidines (T,C) suivent un pattern spécifique."
    
    if correct_positions >= 2:
        return False, f"⚠️ Séquence partiellement correcte ({correct_positions}/4 positions). Réexaminez les dossiers des patients restants. Concentration sur les indices des températures d'échantillon et liaisons hydrogène."
    
    return False, f"❌ Séquence incorrecte : {cleaned_sequence}. Analysez systématiquement chaque dossier patient. Cherchez les indices dans : identifiants (PAT-X00Y), poids moléculaires, heures de prélèvement, et complémentarités Watson-Crick."

# --------- ROOM 5: LABORATOIRE DE CONFINEMENT BIOLOGIQUE 🦠 ---------
# Enigme d'escape game : Déchiffrer les codes de quarantaine

def room5_get_containment_data() -> Dict[str, Any]:
    """Retourne les données pour l'épreuve de confinement biologique"""
    return {
        "situation_critique": {
            "titre": "🦠 LABORATOIRE P4 - BREACH DE CONFINEMENT",
            "description": "Le virus a muté et s'est échappé du laboratoire de confinement de niveau 4. Les systèmes de quarantaine automatique se sont activés, vous enfermant à l'intérieur. Vous devez déchiffrer les codes d'urgence pour déverrouiller les sas de sécurité avant que l'air ne soit purgé.",
            "temps_limite": 300,  # 5 minutes
            "enjeu": "Échec = Activation du protocole de purge - Élimination de toute vie dans le laboratoire"
        },
        
        "indices_laboratoire": [
            {
                "source": "� Microscope électronique",
                "message": "ECHANTILLON_042: Structure virale hexagonale détectée. Taille: 120nm. Pattern géométrique : les angles internes totalisent 720°. Chaque côté mesure 20nm. INDICE: La forme révèle le premier chiffre.",
                "indice_cache": "6",  # Hexagone = 6 côtés
                "explication": "Hexagone = 6 côtés, premier chiffre du code"
            },
            {
                "source": "📊 Analyseur spectroscopique",
                "message": "RAPPORT_FREQ: Fréquence de résonance virale = 2847 Hz. Harmoniques détectées à 2x, 3x et 4x la fréquence fondamentale. Les médecins utilisent cette fréquence depuis 1847 pour stériliser. INDICE: L'année révèle le deuxième chiffre.",
                "indice_cache": "8",  # 1847 -> dernier chiffre significatif médical
                "explication": "1847 = année de découverte des antiseptiques par Semmelweis, chiffre 8"
            },
            {
                "source": "🧪 Centrifugeuse automatique",
                "message": "PROTOCOLE_SPIN: Vitesse de séparation = 3000 RPM. Temps de cycle = 15 minutes. Force centrifuge = 1500g. Tubes disposés en cercle parfait. INDICE: Le nombre de tubes standard révèle le troisième chiffre.",
                "indice_cache": "4",  # 4 tubes standard en centrifugeuse médicale
                "explication": "Configuration standard = 4 tubes, troisième chiffre"
            },
            {
                "source": "🌡️ Moniteur température cryogénique", 
                "message": "ALERTE_TEMP: Échantillons conservés à -196°C (azote liquide). Seuil critique: -180°C. Temps avant dégradation: 120 minutes. Container: format cubique. INDICE: Les faces du container révèlent le quatrième chiffre.",
                "indice_cache": "6",  # Cube = 6 faces
                "explication": "Cube de stockage = 6 faces, quatrième chiffre"
            },
            {
                "source": "� Système injection automatique",
                "message": "CONFIG_DOSE: Seringues prêtes = 9 unités. Volume unitaire = 5mL. Pression = 2 bars. Délai entre injections = 30 secondes. INDICE: Le total des seringues moins la pression révèle le cinquième chiffre.",
                "indice_cache": "7",  # 9 seringues - 2 bars = 7
                "explication": "9 seringues - 2 bars de pression = 7, cinquième chiffre"
            }
        ],
        
        "equipements_bloques": {
            "sas_principal": "🔒 VERROUILLÉ - Code d'urgence requis",
            "ventilation": "⏸️ EN ATTENTE - Purge dans 5 minutes",  
            "systeme_communication": "📡 ISOLÉ - Appels d'urgence bloqués",
            "eclairage_secours": "🔋 AUTONOMIE 4 MIN - Batterie faible",
            "detecteurs_bio": "� ACTIFS - Contamination détectée niveau 4"
        },
        
        "code_sequence": "68467",  # Code final basé sur les 5 indices
        
        "consequences_echec": [
            "� Activation du protocole de purge automatique",
            "☣️ Élimination de toute forme de vie dans le laboratoire",
            "🔥 Incinération complète des échantillons et du personnel",
            "🚫 Scellement permanent du laboratoire P4",
            "📰 Couverture médiatique catastrophique",
            "⚖️ Enquête internationale sur la sécurité biologique"
        ],
        
        "procedure_evacuation": {
            "etape_1": "Saisir le code de déverrouillage d'urgence (5 chiffres)",
            "etape_2": "Activer la séquence de décontamination", 
            "etape_3": "Évacuer par le sas de sécurité principal",
            "etape_4": "Déclencher l'alerte de confinement externe"
        }
    }

def room5_validate_containment_code(code_input: str, start_ts: int, now_ts: int) -> Tuple[bool, str]:
    """Valide le code de confinement avec analyse des indices"""
    data = room5_get_containment_data()
    correct_code = data["code_sequence"]
    
    # Vérification du temps (5 minutes = 300 secondes)
    if start_ts is None or (now_ts - start_ts) > 300:
        temps_ecoule = (now_ts - start_ts) if start_ts else 0
        return False, f"💀 PROTOCOLE DE PURGE ACTIVÉ ! Temps dépassé ({temps_ecoule//60}m {temps_ecoule%60}s / 5m). L'air du laboratoire est purgé. Vous êtes éliminé avec tous les échantillons viraux. Mission échouée."
    
    # Nettoyer l'input
    cleaned_code = code_input.strip().replace(" ", "").replace("-", "")
    
    # Vérifications de base
    if not cleaned_code:
        return False, "⚠️ ERREUR : Code vide. Saisissez le code de déverrouillage d'urgence (5 chiffres)."
    
    if len(cleaned_code) != 5:
        return False, f"⚠️ ERREUR : Code de longueur incorrecte ({len(cleaned_code)} chiffres). Le code d'urgence doit contenir exactement 5 chiffres."
    
    if not cleaned_code.isdigit():
        return False, "⚠️ ERREUR : Code invalide. Utilisez uniquement des chiffres (0-9)."
    
    # Vérification du code complet
    if cleaned_code == correct_code:
        temps_utilise = now_ts - start_ts
        return True, f"🎉 ÉVACUATION RÉUSSIE ! Code de confinement validé : {correct_code}. Temps d'évasion: {temps_utilise//60}m {temps_utilise%60}s. Les sas de sécurité s'ouvrent ! Vous vous échappez du laboratoire P4 juste avant la purge automatique. Le virus reste confiné. Vous avez sauvé l'humanité !"
    
    # Analyse des erreurs partielles pour aider
    correct_positions = sum(1 for i, digit in enumerate(cleaned_code) if i < len(correct_code) and digit == correct_code[i])
    
    if correct_positions >= 4:
        return False, f"🔓 PRESQUE ! {correct_positions}/5 chiffres corrects en bonne position. Un seul chiffre incorrect. Réexaminez attentivement les indices des équipements de laboratoire."
    
    elif correct_positions >= 3:
        return False, f"⚡ PROCHE ! {correct_positions}/5 chiffres corrects. Vérifiez les calculs dans les rapports d'analyse. Chaque équipement révèle un chiffre spécifique."
    
    elif correct_positions >= 2:
        return False, f"🧪 PARTIELLEMENT CORRECT ! {correct_positions}/5 chiffres en bonne position. Analysez systématiquement chaque indice : formes géométriques, années historiques, configurations standard."
    
    elif correct_positions == 1:
        return False, f"🔬 UN DÉBUT ! {correct_positions}/5 chiffre correct. Relisez attentivement tous les messages des équipements. Les indices sont cachés dans les détails techniques."
    
    else:
        return False, f"❌ CODE INCORRECT : {cleaned_code}. Aucun chiffre correct. Examinez méticuleusement chaque rapport d'équipement. Les 5 indices révèlent chaque chiffre dans l'ordre."

# Maintenir compatibilité avec l'ancien système  
FINAL_QUESTIONS = []  # Vide car maintenant c'est un code à saisir
room5_check_answers = lambda answers, start_ts, now_ts: room5_validate_containment_code(answers[0] if answers else "", start_ts, now_ts)

# --------- ROOM 6: CHAMBRE D'ISOLATION DU PATIENT ZÉRO 🏥 ---------
# Enigme d'escape game finale : Créer l'antidote ultime

def room6_get_patient_zero_data() -> Dict[str, Any]:
    """Retourne les données pour l'épreuve finale du patient zéro"""
    return {
        "situation_finale": {
            "titre": "🏥 CHAMBRE D'ISOLATION - PATIENT ZÉRO CRITIQUE",
            "description": "Vous êtes dans la chambre du patient zéro, source de l'épidémie. Son état se dégrade rapidement. Vous devez analyser son ADN viral, déchiffrer les mutations et synthétiser l'antidote parfait avant qu'il ne soit trop tard. C'est votre dernière chance de sauver l'humanité.",
            "temps_limite": 420,  # 7 minutes
            "enjeu": "Échec = Mort du patient zéro et propagation mondiale incontrôlable"
        },
        
        "patient_zero_vitals": {
            "nom": "Dr. Alexander Petrov",
            "age": 52,
            "profession": "Virologue en chef - Laboratoire d'origine",
            "statut": "CRITIQUE - Défaillance multi-organique imminente",
            "temps_restant": "7 minutes avant coma irréversible",
            "symptomes": [
                "Fièvre 42.3°C (seuil létal)",
                "Saturation O2: 78% (critique)", 
                "Rythme cardiaque: 156 bpm (tachycardie sévère)",
                "Pression artérielle: 220/140 (urgence hypertensive)",
                "Conscience: confuse, délire viral"
            ]
        },
        
        "indices_adn_viral": [
            {
                "source": "🧬 Séquenceur génétique principal",
                "mutation_detectee": "SEGMENT_ALPHA",
                "sequence_originale": "ATCG-GCAT-TACG",
                "sequence_mutee": "CTAG-GCTA-TACG", 
                "analyse": "Inversion des 4 premiers nucléotides. Facteur de virulence x3. Résistance aux antiviraux standard. INDICE: Pour neutraliser, inverser la première mutation.",
                "antidote_partiel": "ATCG",  # Inversion de CTAG
                "position_antidote": 1
            },
            {
                "source": "🔬 Microscope confocal avancé", 
                "mutation_detectee": "SEGMENT_BETA",
                "sequence_originale": "CGTA-ATGC-CCGT",
                "sequence_mutee": "CGTA-TACG-CCGT",
                "analyse": "Substitution nucléotidique en position centrale. Échappement immunitaire activé. Cytokine storm déclenché. INDICE: Restaurer la séquence originale du milieu.",
                "antidote_partiel": "ATGC",  # Séquence originale du milieu  
                "position_antidote": 2
            },
            {
                "source": "⚗️ Analyseur protéomique",
                "mutation_detectee": "SEGMENT_GAMMA", 
                "sequence_originale": "TTAA-GGCC-ATCG",
                "sequence_mutee": "TTAA-GGCC-CGTA",
                "analyse": "Permutation circulaire finale. Protéine de surface altérée. Capacité d'infection x10. Létalité 95%. INDICE: Rétablir la configuration originale de fin.",
                "antidote_partiel": "ATCG",  # Séquence originale de fin
                "position_antidote": 3
            }
        ],
        
        "formule_antidote": {
            "sequence_complete": "ATCG-ATGC-ATCG",  # Combinaison des 3 antidotes partiels
            "methode_synthese": [
                "1️⃣ Analyser les 3 mutations virales détectées",
                "2️⃣ Pour chaque segment muté, identifier la correction nécessaire", 
                "3️⃣ Segment Alpha: Inverser CTAG → ATCG",
                "4️⃣ Segment Beta: Restaurer TACG → ATGC", 
                "5️⃣ Segment Gamma: Corriger CGTA → ATCG",
                "6️⃣ Combiner les 3 corrections: ATCG-ATGC-ATCG"
            ],
            "format_attendu": "ATCG-ATGC-ATCG",
            "separateur": "-"
        },
        
        "equipements_medicaux": {
            "respirateur": "⚠️ SURCHARGE - Patient en détresse respiratoire",
            "dialyse": "🔄 ACTIF - Filtration toxines virales", 
            "perfusion": "💉 DEBIT MAX - Cocktail de survie perfusé",
            "moniteur_cardiaque": "📈 ALARME - Arythmie critique détectée",
            "scanner_cerebral": "🧠 OEDEME - Pression intracrânienne élevée"
        },
        
        "laboratoire_urgence": {
            "synthese_moleculaire": "🧪 OPERATIONNEL - Prêt pour antidote",
            "culture_cellulaire": "🦠 CONTAMINEES - Échantillons viraux actifs",
            "centrifugeuse_haute": "⚡ EN MARCHE - Purification en cours",
            "microscope_tunnel": "🔬 ANALYSE - Structure virale temps réel", 
            "incubateur_sterile": "🌡️ 37°C - Conditions optimales maintenues"
        },
        
        "consequences_echec": [
            "💀 Mort du patient zéro dans 7 minutes",
            "🌍 Perte du seul espoir d'antidote universel",  
            "🦠 Propagation virale mondiale incontrôlable",
            "⚰️ Extinction probable de l'humanité en 30 jours",
            "🏥 Effondrement des systèmes de santé mondiaux",
            "🚨 Activation des protocoles d'urgence militaire"
        ]
    }

def room6_validate_antidote_formula(formula_input: str, start_ts: int, now_ts: int) -> Tuple[bool, str]:
    """Valide la formule d'antidote final avec analyse des mutations"""
    data = room6_get_patient_zero_data()
    correct_formula = data["formule_antidote"]["sequence_complete"]
    
    # Vérification du temps (7 minutes = 420 secondes)
    if start_ts is None or (now_ts - start_ts) > 420:
        temps_ecoule = (now_ts - start_ts) if start_ts else 0
        return False, f"💀 PATIENT ZÉRO DÉCÉDÉ ! Temps dépassé ({temps_ecoule//60}m {temps_ecoule%60}s / 7m). Le Dr Petrov sombre dans un coma irréversible. L'antidote ne peut plus être testé. L'humanité est condamnée à l'extinction virale."
    
    # Nettoyer l'input
    cleaned_formula = formula_input.strip().upper().replace(" ", "")
    
    # Vérifications de base
    if not cleaned_formula:
        return False, "⚠️ ERREUR : Formule vide. Saisissez la séquence d'antidote complète (format: XXXX-XXXX-XXXX)."
    
    # Vérifier le format avec tirets
    if not any(sep in cleaned_formula for sep in ['-', '_', '|', ':']):
        return False, "⚠️ ERREUR FORMAT : Séquence doit être séparée en 3 segments (utilisez des tirets: XXXX-XXXX-XXXX)."
    
    # Normaliser les séparateurs
    for sep in ['_', '|', ':', ' ']:
        cleaned_formula = cleaned_formula.replace(sep, '-')
    
    # Vérifier structure
    segments = cleaned_formula.split('-')
    if len(segments) != 3:
        return False, f"⚠️ ERREUR : {len(segments)} segments détectés. L'antidote nécessite exactement 3 segments correctifs (un par mutation)."
    
    # Vérifier chaque segment
    for i, segment in enumerate(segments):
        if len(segment) != 4:
            return False, f"⚠️ SEGMENT {i+1} INVALIDE : {len(segment)} nucléotides. Chaque segment doit contenir 4 nucléotides (A,T,C,G)."
        
        if not all(c in 'ATCG' for c in segment):
            invalid_chars = set(segment) - set('ATCG')
            return False, f"⚠️ SEGMENT {i+1} CORROMPU : Caractères invalides {invalid_chars}. Utilisez uniquement A, T, C, G."
    
    # Vérification finale
    if cleaned_formula == correct_formula:
        temps_utilise = now_ts - start_ts
        return True, f"🎉 ANTIDOTE SYNTHÉTISÉ AVEC SUCCÈS ! Formule validée: {correct_formula}. Temps record: {temps_utilise//60}m {temps_utilise%60}s. Vous injectez l'antidote au Dr Petrov... Sa fièvre chute immédiatement ! Les signes vitaux se stabilisent ! L'humanité est sauvée ! Vous êtes le héros qui a stoppé la pandémie mondiale !"
    
    # Analyse des erreurs par segment pour aider
    correct_segments = correct_formula.split('-')
    errors = []
    correct_count = 0
    
    for i, (user_seg, correct_seg) in enumerate(zip(segments, correct_segments)):
        if user_seg == correct_seg:
            correct_count += 1
        else:
            mutation_name = ["ALPHA", "BETA", "GAMMA"][i]
            errors.append(f"Segment {mutation_name}: {user_seg} → devrait être {correct_seg}")
    
    if correct_count == 2:
        return False, f"🧬 TRÈS PROCHE ! {correct_count}/3 segments corrects. Un seul segment à corriger:\n• {errors[0]}\nRevisez l'analyse de cette mutation spécifique."
    
    elif correct_count == 1:
        return False, f"⚗️ PARTIELLEMENT CORRECT ! {correct_count}/3 segments validés. Corrections nécessaires:\n• {chr(10).join(errors[:2])}\nAnalysez les séquences originales vs mutées."
    
    else:
        return False, f"❌ ANTIDOTE INCORRECT : {cleaned_formula}. Aucun segment correct. Relisez attentivement les 3 analyses de mutations virales. Chaque segment doit corriger une mutation spécifique (Alpha, Beta, Gamma)."
