from abc import ABC, abstractmethod
from model.SudokuBoard import SudokuBoard
import random


class Crossover(ABC):
    def __init__(self, s1: SudokuBoard, s2: SudokuBoard) -> None:
        self.first_parent = s1
        self.second_parent = s2

    @abstractmethod
    def crossover(self) -> SudokuBoard:
        pass


class BasicCrossover(Crossover):
    def __init__(self, s1: SudokuBoard, s2: SudokuBoard) -> None:
        super().__init__(s1, s2)

    def crossover(self) -> SudokuBoard:
        threshold = random.randint(1, 8)
        new_board = SudokuBoard()
        for i in range(0, 9):
            new_board.set_row(i, self.first_parent.row(i) if i < threshold else self.second_parent.row(i))
        return new_board


class OneRowCrossover(Crossover):
    def __init__(self, s1: SudokuBoard, s2: SudokuBoard) -> None:
        super().__init__(s1, s2)

    def crossover(self) -> SudokuBoard:
        row_index = random.randint(0, 8)
        new_board = SudokuBoard()
        for i in range(0, 9):
            new_board.set_row(i, self.first_parent.row(i) if i != row_index else self.second_parent.row(i))
        return new_board
