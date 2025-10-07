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
    patients_data = puzzles.room1_get_patients_data()
    if request.method == "POST":
        try:
            bpm = int(request.form.get("bpm"))
            if puzzles.room1_check_bpm(bpm):
                state["progress"]["room1"] = True
                save_state(state)
                return redirect(url_for("room2"))
            else:
                msg = f"BPM incorrect. Vérifiez votre calcul pour les patients de 68-72 ans."
        except (ValueError, TypeError):
            msg = "Veuillez entrer un nombre valide."
    return render_template("room1.html", patients_data=patients_data, message=msg)

# ---------- ROOM 2 ----------
@app.route("/room/2", methods=["GET", "POST"])
def room2():
    state = load_state()
    r = _check_access_for_room(state, 2)
    if r:
        return r
    msg = None
    prescription_data = puzzles.room2_get_prescription_data()
    if request.method == "POST":
        # Récupérer les prescriptions du formulaire
        prescriptions = {}
        for patient in prescription_data["patients"]:
            nom = patient["nom"]
            medicament = request.form.get(nom, "").strip()
            if medicament:
                prescriptions[nom] = medicament
        
        if len(prescriptions) == len(prescription_data["patients"]):
            ok, info = puzzles.room2_validate_prescriptions(prescriptions)
            msg = info
            if ok:
                state["progress"]["room2"] = True
                save_state(state)
                return redirect(url_for("room3"))
        else:
            msg = "Veuillez prescrire un médicament à chaque patient."
    return render_template("room2.html", prescription_data=prescription_data, message=msg)

# ---------- ROOM 3 ----------
@app.route("/room/3", methods=["GET", "POST"])
def room3():
    state = load_state()
    r = _check_access_for_room(state, 3)
    if r:
        return r
    msg, secret = None, None
    hydration_data = puzzles.room3_get_hydration_data()
    if request.method == "POST":
        # Récupérer les choix d'hydratation du formulaire
        hydration_choices = {}
        for patient in hydration_data["patients"]:
            nom = patient["nom"]
            try:
                water_amount = float(request.form.get(nom, ""))
                hydration_choices[nom] = water_amount
            except (ValueError, TypeError):
                msg = "Veuillez sélectionner une quantité d'eau pour chaque patient."
                break
        
        if not msg and len(hydration_choices) == len(hydration_data["patients"]):
            ok, info = puzzles.room3_validate_hydration(hydration_choices)
            msg = info
            if ok:
                secret = "Hydratation optimisée ! Tous les patients sont stabilisés."
                state["progress"]["room3"] = True
                save_state(state)
                # Redirection vers room4 après succès
                return redirect(url_for("room4"))
    return render_template("room3.html", hydration_data=hydration_data, message=msg, secret=secret)

# ---------- ROOM 4 ----------
@app.route("/room/4", methods=["GET", "POST"])
def room4():
    state = load_state()
    r = _check_access_for_room(state, 4)
    if r:
        return r
    
    # Charger les données génétiques pour l'affichage
    genetic_data = puzzles.room4_get_genetic_data()
    
    msg = None
    if request.method == "POST":
        sequence_input = request.form.get("sequence", "").strip()
        ok, info = puzzles.room4_validate_genetic_sequence(sequence_input)
        msg = info
        if ok:
            state["progress"]["room4"] = True
            save_state(state)
            # Start timer for room5
            state = load_state()
            state["room5_start"] = int(time.time())
            save_state(state)
            return redirect(url_for("room5"))
    
    return render_template("room4.html", genetic_data=genetic_data, message=msg)

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
    containment_data = puzzles.room5_get_containment_data()
    
    if request.method == "POST":
        containment_code = request.form.get("containment_code", "").strip()
        ok, info = puzzles.room5_validate_containment_code(containment_code, state["room5_start"], int(time.time()))
        if ok:
            state["progress"]["room5"] = True
            save_state(state)
            # Start timer for room6
            state = load_state()
            state["room6_start"] = int(time.time())
            save_state(state)
            return redirect(url_for("room6"))
        else:
            msg = info
            # On failure but still within time, let them retry
            if "PROTOCOLE DE PURGE ACTIVÉ" in info:
                return redirect(url_for("fail"))
    
    return render_template("room5.html", containment_data=containment_data, message=msg)

# ---------- ROOM 6 ----------
@app.route("/room/6", methods=["GET", "POST"])
def room6():
    state = load_state()
    r = _check_access_for_room(state, 6)
    if r:
        return r
    if state.get("room6_start") is None:
        # If not started via room5, start now (fallback)
        state["room6_start"] = int(time.time())
        save_state(state)
    
    msg = None
    patient_data = puzzles.room6_get_patient_zero_data()
    
    if request.method == "POST":
        antidote_formula = request.form.get("antidote_formula", "").strip()
        ok, info = puzzles.room6_validate_antidote_formula(antidote_formula, state["room6_start"], int(time.time()))
        if ok:
            state["progress"]["room6"] = True
            save_state(state)
            return redirect(url_for("success"))
        else:
            msg = info
            # On failure but still within time, let them retry
            if "PATIENT ZÉRO DÉCÉDÉ" in info:
                return redirect(url_for("fail"))
    
    return render_template("room6.html", patient_data=patient_data, message=msg)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/fail")
def fail():
    return render_template("fail.html")

if __name__ == "__main__":
    app.run(debug=True)
