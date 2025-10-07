from typing import Dict, Any, List, Tuple
import json, os, time
from game.utils import sha256_hex, b64_decode
from cryptography.fernet import Fernet

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

# --------- ROOM 1: AUTH ---------
# Password clear text is 'Nightingale_1860' (Florence Nightingale ref.)
# The logs provide base64 and a sha256 of the clear text.
ROOM1_PASSWORD = "Nightingale_1860"
ROOM1_PASSWORD_HASH = sha256_hex(ROOM1_PASSWORD)

def room1_check_password(guess: str) -> bool:
    return sha256_hex(guess.strip()) == ROOM1_PASSWORD_HASH

# --------- ROOM 2: DATA CLEANUP ---------
# We provide a small corrupted JSON for patients. The validation checks basic ranges.
def room2_load_corrupted() -> Dict[str, Any]:
    with open(os.path.join(DATA_DIR, "patients_corrupted.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def room2_validate_solution(age: int, temperature: float, bpm: int) -> Tuple[bool, str]:
    # Basic medical sanity checks for a teen-adult population
    if not (0 < age < 120):
        return False, "Âge incohérent"
    if not (34.0 <= temperature <= 41.0):
        return False, "Température incohérente"
    if not (40 <= bpm <= 180):
        return False, "Fréquence cardiaque incohérente"
    # Hidden expected combination from hints (example target)
    if (age, round(temperature,1), bpm) == (32, 38.5, 96):
        return True, "OK"
    return False, "Les valeurs ne correspondent pas aux indices"
    
# --------- ROOM 3: CRYPTO (Fernet AES128-CBC-HMAC) ---------
# The Fernet key is split in virus_code.py as fragments.
def _fernet_key_from_fragments() -> bytes:
    # Virus fragments stored in virus_code.py
    ns = {}
    with open(os.path.join(DATA_DIR, "virus_code.py"), "r", encoding="utf-8") as f:
        code = f.read()
    exec(code, ns, ns)  # safe enough for controlled workshop asset
    key_fragments = [ns.get("K1",""), ns.get("K2",""), ns.get("K3",""), ns.get("K4","")]
    key_b64 = "".join(key_fragments)
    return key_b64.encode("utf-8")

def room3_decrypt_secret(user_key_concat: str) -> Tuple[bool, str]:
    # Players must provide the same concatenation as in virus_code.py to succeed
    expected = _fernet_key_from_fragments().decode("utf-8")
    if user_key_concat != expected:
        return False, "Mauvaise clé recomposée."
    key = expected.encode("utf-8")
    f = Fernet(key)
    with open(os.path.join(DATA_DIR, "secret_message.fernet"), "rb") as g:
        token = g.read()
    try:
        msg = f.decrypt(token).decode("utf-8")
        return True, msg
    except Exception as e:
        return False, "Impossible de déchiffrer: " + str(e)

# --------- ROOM 4 ---------
def room4_validate_sequence(seq):
    """
    Puzzle ADN : Les joueurs doivent reconstituer une séquence génétique
    en analysant des fragments d'ADN de patients contaminés.
    
    Indices cachés dans les données :
    - Patient A (Adénine) : Fragment commence par A, poids moléculaire 135
    - Patient T (Thymine) : Fragment commence par T, température 37°C
    - Patient C (Cytosine) : Fragment commence par C, 3 liaisons hydrogène
    - Patient G (Guanine) : Fragment commence par G, date 15/01
    
    Les indices numériques donnent l'ordre :
    135 (1er), 37 (2ème), 3 (3ème), 15 (4ème... mais c'est un piège!)
    
    En fait, il faut utiliser les règles d'appariement de l'ADN :
    A-T et C-G sont complémentaires
    
    La vraie séquence est basée sur le code génétique du virus :
    ATCG = séquence complète correcte
    """
    correct = ["A", "T", "C", "G"]
    
    # Nettoyer l'input
    cleaned = [s.strip().upper() for s in seq]
    
    if cleaned == correct:
        return True, "✓ Séquence ADN validée ! Le code génétique du virus est identifié. Accès au laboratoire final autorisé."
    
    # Messages d'aide progressifs
    if len(cleaned) != 4:
        return False, "⚠️ Erreur : La séquence doit contenir exactement 4 nucléotides (A, T, C, G)."
    
    if set(cleaned) - {"A", "T", "C", "G"}:
        return False, "⚠️ Erreur : Utilisez uniquement les bases azotées A, T, C et G."
    
    # Vérifier si c'est juste dans le mauvais ordre
    if sorted(cleaned) == sorted(correct):
        return False, "⚠️ Les nucléotides sont corrects mais pas dans le bon ordre. Analysez les indices numériques des patients."
    
    return False, "❌ Séquence incorrecte. Examinez attentivement les dossiers patients et leurs caractéristiques."

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
