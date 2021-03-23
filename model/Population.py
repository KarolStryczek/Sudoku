from typing import List, Tuple

from model.Mutator import Mutator
from model.SudokuBoard import SudokuBoard
import random


class Population:
    def __init__(self, population: List[SudokuBoard], mutator: Mutator) -> None:
        self.population = population
        self.population_size = len(population)
        self.sort_population()
        self.mutator = mutator
        self.requires_sort = False

    def sort_population(self) -> None:
        self.population.sort(key=lambda s: s.calculate_fitness())
        self.requires_sort = False

    def reduce_population(self) -> None:
        self.population = self.population[:self.population_size]

    def add(self, sudoku: SudokuBoard) -> None:
        if sudoku not in self.population:
            self.population.append(sudoku)
            self.requires_sort = True

    def choose_random_parents(self) -> Tuple[SudokuBoard, SudokuBoard]:
        return random.choices(self.population, k=2)

    def update(self) -> None:
        self.sort_population()
        self.reduce_population()
        self.requires_sort = False

    def get_best_fitness(self) -> int:
        if self.requires_sort:
            self.sort_population()
        return self.population[0].calculate_fitness()

    def get_mean_fitness(self) -> float:
        return sum([sudoku.calculate_fitness() for sudoku in self.population]) / len(self.population)

    def mutate(self) -> None:
        # print(f"Mutating. Best = {self.population[0].calculate_fitness()}")
        self.sort_population()
        for sudoku in self.population[10:]:
            if random.randint(0, 99) < 20:
                # print(f"Mutating. CURRENT = {sudoku.calculate_fitness()}")
                self.mutator.mutate(sudoku)
        self.sort_population()
