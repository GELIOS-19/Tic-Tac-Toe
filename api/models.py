from typing import List


# player model
class Player:
    # constants
    X_PLAYER = "x"
    O_PLAYER = "o"
    NULL_PLAYER = ""

    mark: str

    # custom dictionary
    @property
    def dictionary(self):
        return {"mark": self.mark, "opposite": self.opposite}

    def __init__(self, mark):
        self.mark = mark

    # returns the opposite player
    @property
    def opposite(self):
        if self.mark == self.X_PLAYER:
            return self.O_PLAYER
        elif self.mark == self.O_PLAYER:
            return self.X_PLAYER
        else:
            return self.NULL_PLAYER


# cell model
class Cell:
    index: int
    player: Player
    filled: bool

    def __init__(self, index, player, filled):
        self.index = index
        self.player = player
        self.filled = filled

    # custom dictionary
    @property
    def dictionary(self):
        return {
            "index": self.index,
            "filled": self.filled,
            "player": self.player.dictionary,
        }


# board model
class Board:
    cells: List[Cell]
    current_player: Player

    def __init__(self, cells, current_player):
        self.cells = cells
        self.current_player = current_player
