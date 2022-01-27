from .models import *
from .board_service import BoardService


class GameService:
  # members
  completed: bool
  winner: Player
  round_count: int

  def __init__(self):
    self.completed = False
    self.winner = Player(Player.NULL_PLAYER)
    self.round_count = 0
    # create new instance board service
    self.board_service = BoardService()

  # get the status of game service
  @property
  def dictionary(self):
    return {
      "completed": self.completed, "winner": self.winner.dictionary, "round_count": self.round_count, "board": {
        "current_player": self.board_service.board.current_player.dictionary, "cells": [cell.dictionary for cell in self.board_service.board.cells],
      },
    }

  # create a new game
  def initialize_game(self):
    self.__init__()

  # player turn
  def player_turn(self, index: int, current_player: Player):
    if not self.board_service.board.cells[index].filled:
      # change cell player
      self.board_service.change_cell_player(index=index, player=current_player)
      # change turn
      self.board_service.change_turn(Player(current_player.opposite))
      # increment round count
      self.round_count += 1
      # check winners
      check = self.board_service.check_winner(player=Player(Player.X_PLAYER), round_count=self.round_count)
      self.completed = check["completed"]
      self.winner = check["winner"]
      if self.completed:
        return
      check = self.board_service.check_winner(player=Player(Player.O_PLAYER), round_count=self.round_count)
      self.completed = check["completed"]
      self.winner = check["winner"]
      if self.completed:
        return
