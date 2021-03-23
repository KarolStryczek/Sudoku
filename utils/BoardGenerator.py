from model.SudokuBoard import SudokuBoard
from utils.Helper import Helper
from typing import List


class BoardGenerator:
    def __init__(self, board: SudokuBoard) -> None:
        self.base_board = board

    def generate_population(self, population_size) -> List[SudokuBoard]:
        population = list()
        for i in range(0, population_size):
            new_candidate = Helper(self.base_board).generate_candidate()
            if new_candidate not in population:
                population.append(new_candidate)
        return population
