from flask import Flask, render_template, request, redirect, url_for
import time, json, os
from game import puzzles
from game.state import load_state, save_state, reset_state

app = Flask(__name__)

# Total allowed time for the whole escape game (35 minutes)
TOTAL_GAME_SECONDS = 35 * 60


@app.context_processor
def inject_state():
    """Make the current game state available in every template as `state`.
    This lets the base layout show the team name and progress without each
    view needing to pass it explicitly.
    """
    try:
        s = load_state()
    except Exception:
        s = {}
    # compute remaining time for the UI
    try:
        started = s.get("started_at")
        if started:
            now = int(time.time())
            left = TOTAL_GAME_SECONDS - (now - int(started))
            if left < 0:
                left = 0
            mins = left // 60
            secs = left % 60
            s["time_left_seconds"] = int(left)
            s["time_left_str"] = f"{mins}:{secs:02d}"
            s["time_up"] = (left == 0)
        else:
            s["time_left_seconds"] = None
            s["time_left_str"] = None
            s["time_up"] = False
    except Exception:
        s["time_left_seconds"] = None
        s["time_left_str"] = None
        s["time_up"] = False
    return dict(state=s)


def _check_access_for_room(state: dict, room_number: int):
    """Return a redirect response if player shouldn't access this room.
    - If game not started, send to index
    - If total time expired, send to fail
    - If previous room(s) incomplete, send to the first incomplete room
    Otherwise return None
    """
    if not state:
        return redirect(url_for("index"))
    started = state.get("started_at")
    if not started:
        return redirect(url_for("index"))
    now = int(time.time())
    if (now - int(started)) > TOTAL_GAME_SECONDS:
        return redirect(url_for("fail"))

    # ensure all previous rooms done (explicit numeric loop)
    for n in range(1, room_number):
        key = f"room{n}"
        if not state.get("progress", {}).get(key):
            # redirect to the first incomplete room
            return redirect(url_for(f"room{n}"))
    return None

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    team_name = request.form.get("team_name", "").strip() or None
    reset_state(team_name)
    return redirect(url_for("lobby"))


@app.route("/reset", methods=["POST"])
def reset():
    """Reset the current game state (useful for demos/tests).
    This is intentionally simple; it resets with no team name.
    """
    reset_state(None)
    return redirect(url_for("index"))

@app.route("/lobby", methods=["GET"])
def lobby():
    state = load_state()
    # Compute server-side remaining time to be authoritative
    started = state.get("started_at")
    if started:
        now = int(time.time())
        if (now - int(started)) > TOTAL_GAME_SECONDS:
            return redirect(url_for("fail"))
    return render_template("lobby.html", state=state)

# ---------- ROOM 1 ----------
@app.route("/room/1", methods=["GET", "POST"])
def room1():
    state = load_state()
    r = _check_access_for_room(state, 1)
    if r:
        return r
    msg = None
    logs = open(os.path.join("data", "logs.txt"), "r", encoding="utf-8").read()
    if request.method == "POST":
        pw = request.form.get("password", "").strip()
        if puzzles.room1_check_password(pw):
            state["progress"]["room1"] = True
            save_state(state)
            return redirect(url_for("room2"))
        else:
            msg = "Mot de passe incorrect."
    return render_template("room1.html", logs=logs, message=msg)

# ---------- ROOM 2 ----------
@app.route("/room/2", methods=["GET", "POST"])
def room2():
    state = load_state()
    r = _check_access_for_room(state, 2)
    if r:
        return r
    msg = None
    corrupted = json.dumps(puzzles.room2_load_corrupted(), ensure_ascii=False, indent=2)
    if request.method == "POST":
        try:
            age = int(request.form.get("age"))
            temperature = float(request.form.get("temperature"))
            bpm = int(request.form.get("bpm"))
        except Exception:
            age, temperature, bpm = 0, 0, 0
        ok, info = puzzles.room2_validate_solution(age, temperature, bpm)
        msg = info
        if ok:
            state["progress"]["room2"] = True
            save_state(state)
            return redirect(url_for("room3"))
    return render_template("room2.html", corrupted=corrupted, message=msg)

# ---------- ROOM 3 ----------
@app.route("/room/3", methods=["GET", "POST"])
def room3():
    state = load_state()
    r = _check_access_for_room(state, 3)
    if r:
        return r
    msg, secret = None, None
    virus_code = open(os.path.join("data", "virus_code.py"), "r", encoding="utf-8").read()
    if request.method == "POST":
        key = request.form.get("key", "").strip()
        ok, res = puzzles.room3_decrypt_secret(key)
        if ok:
            secret = res
            state["progress"]["room3"] = True
            save_state(state)
        else:
            msg = res
    return render_template("room3.html", virus_code=virus_code, message=msg, secret=secret)

# ---------- ROOM 4 ----------
@app.route("/room/4", methods=["GET", "POST"])
def room4():
    state = load_state()
    r = _check_access_for_room(state, 4)
    if r:
        return r
    msg = None
    if request.method == "POST":
        raw = request.form.get("seq", "").replace(" ", "")
        seq = [x for x in raw.split(",") if x]
        ok, info = puzzles.room4_validate_sequence(seq)
        msg = info
        if ok:
            state["progress"]["room4"] = True
            save_state(state)
            # Start timer for room5
            state = load_state()
            state["room5_start"] = int(time.time())
            save_state(state)
            return redirect(url_for("room5"))
    return render_template("room4.html", message=msg)

# ---------- ROOM 5 ----------
@app.route("/room/5", methods=["GET", "POST"])
def room5():
    state = load_state()
    r = _check_access_for_room(state, 5)
    if r:
        return r
    if state.get("room5_start") is None:
        # If not started via room4, start now (fallback)
        state["room5_start"] = int(time.time())
        save_state(state)
    msg = None
    questions = puzzles.FINAL_QUESTIONS
    if request.method == "POST":
        answers = [request.form.get(f"q{i}", "") for i in range(len(questions))]
        ok, info = puzzles.room5_check_answers(answers, state["room5_start"], int(time.time()))
        if ok:
            state["progress"]["room5"] = True
            save_state(state)
            return redirect(url_for("success"))
        else:
            msg = info
            # On failure but still within time, let them retry
            if "Temps dépassé" in info:
                return redirect(url_for("fail"))
    return render_template("room5.html", questions=questions, message=msg)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/fail")
def fail():
    return render_template("fail.html")

if __name__ == "__main__":
    app.run(debug=True)
