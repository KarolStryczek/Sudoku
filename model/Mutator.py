from abc import ABC, abstractmethod
from model.SudokuBoard import SudokuBoard
import random


class Mutator(ABC):
    def __init__(self) -> None:
        self.base_sudoku = None

    def set_base_board(self, base_sudoku: SudokuBoard) -> None:
        self.base_sudoku = base_sudoku

    @abstractmethod
    def mutate(self, sudoku: SudokuBoard) -> None:
        pass


class RandomInRowMutator(Mutator):
    def mutate(self, sudoku: SudokuBoard) -> None:
        row = random.randint(0, 8)
        not_filled_indexes = [i for i in range(0, 9) if self.base_sudoku.element(row, i) != 0]
        col1, col2 = random.choices(not_filled_indexes, k=2)
        sudoku.swap_elements_in_row(row, col1, col2)


class LazyMutator(Mutator):
    def mutate(self, sudoku: SudokuBoard) -> None:
        pass


class SmartDuplicatesColumnMutator(Mutator):
    def mutate(self, sudoku: SudokuBoard) -> None:
        row = random.randint(0, 8)
        not_filled_indexes = [i for i in range(0, 9) if self.base_sudoku.element(row, i) != 0]
        for col in not_filled_indexes:
            element = sudoku.element(row, col)
            if element in sudoku.column(col):
                not_filled_indexes.remove(col)
                sudoku.swap_elements_in_row(row, col, random.choice(not_filled_indexes))
