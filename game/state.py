import json, os, threading, time
from typing import Dict, Any

STATE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "game_state.json")
_lock = threading.Lock()

DEFAULT_STATE = {
    "team_name": None,
    "started_at": None,
    "progress": { "room1": False, "room2": False, "room3": False, "room4": False, "room5": False, "room6": False },
    "room5_start": None,
    "room6_start": None,
    "roles": {}  # role -> player name
}

def load_state() -> Dict[str, Any]:
    if not os.path.exists(STATE_FILE):
        save_state(DEFAULT_STATE)
    with _lock, open(STATE_FILE, "r", encoding="utf-8") as f:
        st = json.load(f)

    # Migration / ensure keys exist for newer versions (e.g. room6)
    changed = False
    if "progress" not in st:
        st["progress"] = DEFAULT_STATE["progress"].copy()
        changed = True
    else:
        for k, v in DEFAULT_STATE["progress"].items():
            if k not in st["progress"]:
                st["progress"][k] = v
                changed = True

    # Ensure room5_start/room6_start keys exist
    if "room5_start" not in st:
        st["room5_start"] = DEFAULT_STATE.get("room5_start")
        changed = True
    if "room6_start" not in st:
        st["room6_start"] = DEFAULT_STATE.get("room6_start")
        changed = True

    if changed:
        save_state(st)

    return st

def save_state(state: Dict[str, Any]) -> None:
    with _lock, open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def reset_state(team_name: str = None) -> Dict[str, Any]:
    st = DEFAULT_STATE.copy()
    st["team_name"] = team_name
    save_state(st)
    return st
