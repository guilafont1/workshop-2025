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
