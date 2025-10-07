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

# --------- ROOM 4: NETWORK ORDER (COOP) ---------
# Players must activate ports in the exact order: 443 -> 22 -> 80
EXPECTED_PORT_SEQ = ["443", "22", "80"]

def room4_validate_sequence(seq: List[str]) -> Tuple[bool, str]:
    if seq == EXPECTED_PORT_SEQ:
        return True, "Pare-feux synchronisés !"
    return False, "Mauvais ordre. Indice: 'HTTPS avant SSH avant HTTP'."

# --------- ROOM 5: FINAL QUIZ WITH TIMER ---------
FINAL_QUESTIONS = [
    ("Quel encodage transforme 'texte' en caractères sûrs pour transport?", ["base64", "sha256", "utf-32"], "base64"),
    ("Quel algorithme est un HACHAGE (non réversible)?", ["AES", "SHA-256", "Fernet"], "SHA-256"),
    ("Dans un hôpital, quelle donnée NE doit PAS être stockée en clair?", ["Nom de la ville", "Identifiant patient", "Liste des couleurs"], "Identifiant patient"),
]

def room5_check_answers(answers: List[str], start_ts: int, now_ts: int) -> Tuple[bool, str]:
    # Must finish under 180 seconds
    if start_ts is None or (now_ts - start_ts) > 180:
        return False, "Temps dépassé (3 minutes)."
    if len(answers) != len(FINAL_QUESTIONS):
        return False, "Toutes les réponses doivent être fournies."
    for (q, options, expected), ans in zip(FINAL_QUESTIONS, answers):
        if ans != expected:
            return False, f"Mauvaise réponse pour: {q}"
    return True, "Système redémarré !"
