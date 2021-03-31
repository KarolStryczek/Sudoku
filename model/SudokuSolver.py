from model.Mutator import Mutator
from model.Population import Population
from utils.BoardGenerator import BoardGenerator
from model.Crossover import *
import pickle


class SudokuSolver:
    def __init__(self, sudoku_base: SudokuBoard, population_size: int, cross_per_iter: int, mutator: Mutator) -> None:
        self.sudoku_base = sudoku_base
        mutator.set_base_board(sudoku_base)
        self.population = Population(BoardGenerator(self.sudoku_base).generate_population(population_size), mutator)
        self.cross_per_iter = cross_per_iter

    def mock_start_pops(self) -> None:
        # mocking starting populations:
        file_path = r'./input/mocking_start_pops/mock_start_0.txt'
        self.population.save_population(file_path)
        print('List of sudoku boards (mocking starting populations) - writing to a file test:')
        print(len(pickle.load(open(file_path, 'rb'))))
        print(pickle.load(open(file_path, 'rb')))
        

    def solve(self, max_iter: int = 200, max_no_improve: int = 10) -> None:
        current_best_fitness = 1e6
        no_improve_count = 0
        for iteration in range(0, max_iter):
            for crossover_number in range(0, self.cross_per_iter):
                p1, p2 = self.population.choose_random_parents()
                self.population.add(RandomCrossover(p1, p2).crossover())
            self.population.update()
            new_best_fitness = self.population.get_best_fitness()
            print(f'iteration: {self.population.get_best_fitness()}, {self.population.get_mean_fitness()}')
            if new_best_fitness < current_best_fitness:
                current_best_fitness = new_best_fitness
                no_improve_count = 0
            else:
                no_improve_count += 1
                if no_improve_count > max_no_improve // 2:
                    print(f'Mutation BEFORE: {self.population.get_best_fitness()}, {self.population.get_mean_fitness()}')
                    self.population.mutate()
                    print(f'Mutation AFTER: {self.population.get_best_fitness()}, {self.population.get_mean_fitness()}')
            if current_best_fitness == 0:
                break
            if no_improve_count >= max_no_improve:
                pass  # TODO BREAK
        print(f'result: {self.population.get_best_fitness()}, {self.population.get_mean_fitness()}')

