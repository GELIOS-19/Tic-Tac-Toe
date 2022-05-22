from typing import List


class Player:
  X_PLAYER = "x"
  O_PLAYER = "o"
  NULL_PLAYER = ""

  mark: str

  @property
  def dictionary(self):
    return {"mark": self.mark, "opposite": self.opposite}

  def __init__(self, mark):
    self.mark = mark

  @property
  def opposite(self):
    if self.mark == self.X_PLAYER:
      return self.O_PLAYER
    elif self.mark == self.O_PLAYER:
      return self.X_PLAYER
    else:
      return self.NULL_PLAYER


class Cell:
  index: int
  player: Player
  filled: bool

  def __init__(self, index, player, filled):
    self.index = index
    self.player = player
    self.filled = filled

  @property
  def dictionary(self):
    return {
        "index": self.index,
        "filled": self.filled,
        "player": self.player.dictionary
    }


class Board:
  cells: List[Cell]
  current_player: Player

  def __init__(self, cells, current_player):
    self.cells = cells
    self.current_player = current_player
