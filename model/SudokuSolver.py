from model.Mutator import Mutator
from model.Population import Population
from utils.BoardGenerator import BoardGenerator
from model.Crossover import *
from utils.LogUtils import m_logger, log_to_all
from typing import List
import matplotlib.pyplot as plt
from datetime import datetime


class SudokuSolver:
    def __init__(self, sudoku_base: SudokuBoard, population_size: int, cross_per_iter: int, mutator: Mutator) -> None:
        self.sudoku_base = sudoku_base
        self.population_size = population_size
        self.population = None
        self.cross_per_iter = cross_per_iter
        self.mutator = mutator
        mutator.set_base_board(sudoku_base)

    def create_start_population(self) -> None:
        self.population = Population(BoardGenerator(self.sudoku_base).generate_population(self.population_size), self.mutator)

    def mock_start_pops(self, sudoku_num: int) -> None:
        # mocking starting populations:
        file_path = rf'./input/mocking_start_pops/mock_start_{sudoku_num}.pkl'
        self.population.save_population(file_path, self.sudoku_base)

    def read_mock_start_pops(self, population: List[SudokuBoard]) -> None:
        self.population = Population(population, self.mutator)

    def solve(self, max_iter: int = 200, max_no_improve: int = 10) -> None:
        current_best_fitness = 1e6
        no_improve_count = 0
        results = list()
        for iteration in range(0, max_iter):
            results.append((self.population.get_best_fitness(), self.population.get_mean_fitness()))
            print(f'{iteration}/{max_iter}')
            for crossover_number in range(0, self.cross_per_iter):
                p1, p2 = self.population.choose_random_parents()
                self.population.add(RandomCrossover(p1, p2).crossover())
            self.population.update()
            new_best_fitness = self.population.get_best_fitness()
            log_to_all(f'iteration:  {iteration}, best: {self.population.get_best_fitness()}, mean: {self.population.get_mean_fitness()}')
            if new_best_fitness < current_best_fitness:
                current_best_fitness = new_best_fitness
                no_improve_count = 0
            else:
                no_improve_count += 1
                if no_improve_count > max_no_improve // 2:
                    m_logger.info(f'Mutation BEFORE: {self.population.get_best_fitness()}, {self.population.get_mean_fitness()}')
                    self.population.mutate()
                    m_logger.info(f'Mutation AFTER: {self.population.get_best_fitness()}, {self.population.get_mean_fitness()}')
            if current_best_fitness == 0:
                break
            if no_improve_count >= max_no_improve:
                pass  # TODO BREAK
        log_to_all(f'result: {self.population.get_best_fitness()}, {self.population.get_mean_fitness()}')
        plt.plot(range(0, max_iter), results)
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.legend(["Best", "Mean"])
        filename = rf'img/result-{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.png'
        plt.savefig(filename)
        plt.show()
