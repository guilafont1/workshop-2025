import json, os, threading, time
from typing import Dict, Any

STATE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db", "game_state.json")
_lock = threading.Lock()

DEFAULT_STATE = {
    "team_name": None,
    "started_at": None,
    "progress": { "room1": False, "room2": False, "room3": False, "room4": False, "room5": False , "room6": False },
    "room6_start": None,
    "roles": {}  # role -> player name
}

def load_state() -> Dict[str, Any]:
    if not os.path.exists(STATE_FILE):
        save_state(DEFAULT_STATE)
    with _lock, open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_state(state: Dict[str, Any]) -> None:
    with _lock, open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def reset_state(team_name: str = None) -> Dict[str, Any]:
    st = DEFAULT_STATE.copy()
    st["team_name"] = team_name
    st["started_at"] = int(time.time())
    save_state(st)
    return st
