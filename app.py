import random
import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

COVEN_ROSTER = {
    "SHALOM": "(brown chocolate)",
    "TIMOTHY": "(grape fruit)",
    "WILSON": "(tall glass of champagne)",
    "RUME": "(baby girl)",
    "MALIK": "(PERFECT SACRIFICE)",
}

GABBY_NAMES = ["GABBY", "GABRIELLA"]
QUEEN_MOTHER_NAMES = [
    "ROSEMARY",
    "SHE ROSE",
    "ROSIE",
    "AFRO",
    "ROSSIE",
    "ROSSY",
    "ROSE",
]
BEAUTIFUL_MAN_NAMES = ["NIFEMI", "NIFE"]

FRIENDS_AND_BLESSINGS = [
    {
        "friend": "SHALOM",
        "action": (
            "Sends you massive warm virtual hugs 🤗, orders hot peppered snail"
            " and chilled malt to sweeten your day. No condition is permanent,"
            " my person! Keep pushing, e go better!"
        ),
    },
    {
        "friend": "TIMOTHY",
        "action": (
            "Wraps you in a tight, reassuring bear hug 🤗 and buys you hot"
            " local Ofada rice with plenty shuku. Chai, see grace! You are"
            " doing well, no dulling!"
        ),
    },
    {
        "friend": "WILSON",
        "action": (
            "Pulls you close for a warm brotherly hug 🤗, drops sweet encouraging"
            " words in your ear, and treats you to hot peppersoup and chilled"
            " zobo. Tension no dey! You will make it!"
        ),
    },
    {
        "friend": "RUME",
        "action": (
            "Gives you soft, cozy hugs 🤗 like baby girl treatment, and orders"
            " sweet, hot puff-puff and cold malt for you. Soft life is your"
            " portion, my gee!"
        ),
    },
    {
        "friend": "MALIK",
        "action": (
            "Gives you a solid protective hug 🤗, says sweet motivational prayers"
            " for your hustle, and credits your energy with hot plantain and"
            " turkey. Wahala for who no believe in you!"
        ),
    },
    {
        "friend": "ROSEMARY",
        "action": (
            "The Queen Mother herself opens her arms for a deep, comforting hug"
            " 🤗, speaks heavy life-changing words into your destiny, and"
            " orders hot spicy suya with chilled Chapman. You are unstoppable!"
        ),
    },
    {
        "friend": "NIFEMI",
        "action": (
            "Sends you sweet encouraging vibes, tight warm hugs 🤗, and buys"
            " you hot bole and fish with extra Titus sauce. Blessings upon"
            " blessings, your hustle must pay!"
        ),
    },
    {
        "friend": "GABBY",
        "action": (
            "Wraps you in tight sisterly hugs 🤗, reminds you that you are too"
            " precious to stress, and orders hot meatpie with cold Hollandia"
            " yoghurt. Joy will locate you today!"
        ),
    },
    {
        "friend": "THE COVEN ANCESTORS",
        "action": (
            "Send spiritual chest rubs and warm ancestral hugs 🤗, assuring you"
            " that your debit alerts will soon turn to multi-million credit"
            " alerts. Amen somebody!"
        ),
    },
]

PUNISHMENTS = [
    (
        "is sentenced to trek barefoot from CMS to Ojuelegba under heavy Lagos"
        " sun while carrying a basket of iced pure water."
    ),
    (
        "must hawk cold Gala and Lacasera in heavy Oshodi traffic without"
        " collecting change from anybody."
    ),
    (
        "is banned from eating hot jollof rice and must feed strictly on dry"
        " garri and tap water for three market days."
    ),
    (
        "must stand at the bus stop and shout 'Ikeja under bridge! Last bus!'"
        " until NEPA/PHED restores light."
    ),
    (
        "is sentenced to peel raw bitter yam and local onions without wiping"
        " their eyes until tears flood the entire coven."
    ),
    (
        "must spend three hours trying to explain quantum physics to a very"
        " stubborn Danfo driver at Yaba bus stop."
    ),
    (
        "is cursed to use a phone with 1% battery while tracking a dispatch"
        " rider who swore he is 'just two blocks away' in Lekki traffic."
    ),
    (
        "must chew the hardest dry Kponmo without drinking water while"
        " listening to a generator knocking its piston right next to their"
        " ear."
    ),
    (
        "is sentenced to bargain for tomatoes in Mile 12 market without"
        " shouting 'Ah, ha! Aunty/Oga make we do half price!'"
    ),
]


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/coven-music-stream")
def coven_music_stream():
  tracks = ["ambient.mp3", "horror.mp3"]
  return jsonify({"track": random.choice(tracks)})


@app.route("/check-coven", methods=["POST"])
def check_coven():
  try:
    data = request.get_json(silent=True) or {}
  except Exception:
    data = {}

  raw_name = data.get("name", "")

  # 1. Reject non-string data types (integers, floats, booleans, lists, objects)
  if not isinstance(raw_name, str):
    return jsonify({
        "status": "error",
        "message": (
            "The void rejects corrupt data types! Enter a name using mortal"
            " letters, try again or pay with your soul..."
        ),
    })

  clean_name = raw_name.strip()

  # 2. Check for empty input after whitespace removal
  if not clean_name:
    return jsonify({
        "status": "error",
        "message": "The void hears nothing! Speak your name to proceed.",
    })

  # 3. Handle symbols: If input contains symbols/numbers (@, #, $, 1, 2, 3, etc.)
  if not re.match(r"^[A-Za-z\s]+$", clean_name):
    return jsonify({
        "status": "error",
        "message": (
            "No dark symbols, numbers, or cursed characters allowed! Only"
            " letters of the mortal alphabet. Try again or pay..."
        ),
    })

  name = clean_name.upper()

  # 4. Match against Coven Roster
  if name in COVEN_ROSTER:
    return jsonify({
        "status": "coven",
        "message": f"WELCOME {name} {COVEN_ROSTER[name]}, YOU ARE IN THE COVEN.",
    })
  elif name in GABBY_NAMES:
    return jsonify({
        "status": "coven",
        "message": f"WELCOME {name} (caramel skin), YOU ARE IN THE COVEN.",
    })
  elif name in QUEEN_MOTHER_NAMES:
    return jsonify({
        "status": "coven",
        "message": f"WELCOME {name} (QUEEN MOTHER), YOU ARE IN THE COVEN.",
    })
  elif name in BEAUTIFUL_MAN_NAMES:
    return jsonify({
        "status": "coven",
        "message": f"WELCOME {name} (beautiful man), YOU ARE IN THE COVEN.",
    })
  else:
    return jsonify({
        "status": "outsider",
        "message": (
            f"YOU ARE NOT IN THE COVEN, {name}. Careful now, you may be"
            " sacrificed..."
        ),
    })


@app.route("/coven-friend", methods=["GET"])
def coven_friend():
  chosen = random.choice(FRIENDS_AND_BLESSINGS)
  return jsonify(chosen)


@app.route("/coven-punishment", methods=["POST"])
def coven_punishment():
  try:
    data = request.get_json(silent=True) or {}
  except Exception:
    data = {}

  target = data.get("target", "MEMBER").upper()
  punishment_text = random.choice(PUNISHMENTS)
  decree = f"By order of the Queen Mother's Tribunal, {target} {punishment_text}"
  return jsonify({"punishment": decree})


if __name__ == "__main__":
  app.run(debug=True)