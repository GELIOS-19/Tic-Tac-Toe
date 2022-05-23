from flask import *
from api import *

# app setup
app = Flask(__name__, template_folder="templates")

# create game service instance
_game_service = GameService()


# game - initialize a game
@app.route("/game/initialize-game")
def initialize_game():
  _game_service.initialize_game()
  return jsonify(game=_game_service.dictionary)


# game - player turn
@app.route("/game/player-turn/<index>/<player>")
def player_turn(player: str, index: int):
  _game_service.player_turn(int(index), Player(player))
  return jsonify(game=_game_service.dictionary)


# game - get unchanged game object
@app.route("/game")
def game():
  return jsonify(game=_game_service.dictionary)


# view - index
@app.route("/")
def index():
  return render_template("index.html", game=_game_service)
