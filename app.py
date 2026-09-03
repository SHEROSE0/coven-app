import os
import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# List of available audio tracks in your static folder
COVEN_MUSIC_TRACKS = ["ambient.mp3", "horror.mp3"]


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/coven-music-stream")
def get_coven_music():
  selected_track = random.choice(COVEN_MUSIC_TRACKS)
  return jsonify({"track": selected_track})


@app.route("/check-coven", methods=["POST"])
def check_coven():
  data = request.get_json()
  name = data.get("name", "").strip().upper()
  return jsonify(
      {"status": "coven", "message": f"Welcome back to the sanctum, {name}."}
  )


@app.route("/coven-friend")
def coven_friend():
  friends = [
      {"friend": "SHALOM", "action": "Grants you safe passage through the mist."},
      {"friend": "TIMOTHY", "action": "Shares a vial of protective elixir."},
  ]
  return jsonify(random.choice(friends))


@app.route("/coven-punishment", methods=["POST"])
def coven_punishment():
  data = request.get_json()
  target = data.get("target", "THE OUTSIDER")
  punishments = [
      f"{target} shall be banished to the endless shadow realm.",
      f"{target} must walk barefoot through the valley of thorns.",
  ]
  return jsonify({"punishment": random.choice(punishments)})


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port, debug=True)