from model.SudokuBoard import SudokuBoard
import random


# TODO make helper reusable
class Helper:
    def __init__(self, board: SudokuBoard):
        self.helper_board = [[None for j in range(0, 9)] for i in range(0, 9)]
        for i in range(0, 9):
            for j in range(0, 9):
                if board.element(i, j) != 0:
                    self.helper_board[i][j] = board.element(i, j)
                else:
                    candidates = list()
                    row = board.row(i)
                    for candidate in range(1, 10):
                        if candidate not in row:
                            candidates.append(candidate)
                    self.helper_board[i][j] = candidates

    def mark_as_used(self, row_index: int, number: int) -> None:
        for i in range(0, 9):
            if type(self.helper_board[row_index][i]) is list:
                self.helper_board[row_index][i].remove(number)

    def generate_candidate(self) -> SudokuBoard:
        candidate_board = SudokuBoard()
        for i in range(0, 9):
            for j in range(0, 9):
                helper_element = self.helper_board[i][j]
                if type(helper_element) is int:
                    candidate_board.set_element(i, j, helper_element)
                elif type(helper_element) is list:
                    if len(helper_element) > 0:
                        random_element = helper_element[random.randint(0, len(helper_element)-1)]
                        candidate_board.set_element(i, j, random_element)
                        self.mark_as_used(i, random_element)
                    else:
                        raise Exception("I am not working correctly. Fix me please")
        return candidate_board
