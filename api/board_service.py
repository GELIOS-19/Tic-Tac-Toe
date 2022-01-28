from .models import *


class BoardService:
  def __init__(self, board_side_length=3):
    self.board_side_length = board_side_length
    self.total_squares = self.board_side_length * self.board_side_length

    # create a new instance of a board
    self.board = Board(cells=[
      Cell(index=i, player=Player(Player.NULL_PLAYER), filled=False) for i in
      range(self.total_squares)], current_player=Player(Player.X_PLAYER))

  @property
  def winning_position_sets(self):
    # winning positions
    winning_position_sets = []
    # three kinds of sets
    horizontal_sets = []
    vertical_sets = []
    diagonal_sets = []
    # get horizontal sets
    horizontal_set = []
    for i in range(self.total_squares):
      horizontal_set.append(i)
      if len(horizontal_set) == self.board_side_length:
        horizontal_sets.append(horizontal_set)
        horizontal_set = []
    # get vertical sets relative to horizontal sets
    vertical_set = []
    for j in range(self.board_side_length):
      for horizontal_set in horizontal_sets:
        vertical_set.append(horizontal_set[j])
        if len(vertical_set) == self.board_side_length:
          vertical_sets.append(vertical_set)
          vertical_set = []
    # get diagonal_sets relative to horizontal sets
    diagonal_set = []
    for k, horizontal_set in enumerate(horizontal_sets):
      diagonal_set.append(horizontal_set[k])
    diagonal_sets.append(diagonal_set)
    diagonal_set = []
    for l, horizontal_set in enumerate(horizontal_sets):
      diagonal_set.append(horizontal_set[len(horizontal_set) - l - 1])
    diagonal_sets.append(diagonal_set)
    # add all the sets to winning_positions_sets
    for horizontal_set in horizontal_sets:
      winning_position_sets.append(horizontal_set)
    for vertical_set in vertical_sets:
      winning_position_sets.append(vertical_set)
    for diagonal_set in diagonal_sets:
      winning_position_sets.append(diagonal_set)
    return winning_position_sets

  def change_cell_player(self, index, player):
    self.board.cells[index].player = player
    self.board.cells[index].filled = True

  def change_turn(self, player: Player):
    self.board.current_player = player

  def check_winner(self, player, round_count):
    for winning_position_set in self.winning_position_sets:
      # check if winning positions are equal to player positions
      conditions = [
        self.board.cells[winning_position_set[i]].player.mark == player.mark
        for i in range(self.board_side_length)]
      true_count = 0
      for condition in conditions:
        if condition:
          true_count += 1
      # set completed status and who the winner is
      if true_count == self.board_side_length:
        return {"completed": True, "winner": player}
    # check for draw
    if round_count > self.total_squares - 1:
      return {"completed": True, "winner": Player(Player.NULL_PLAYER)}
    # return negative response if no winner
    return {"completed": False, "winner": Player(Player.NULL_PLAYER)}
