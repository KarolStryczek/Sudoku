from typing import List, Tuple

from utils.LogUtils import m_logger
from model.Mutator import Mutator
from model.SudokuBoard import SudokuBoard
import random
import pickle
import re


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
        m_logger.info(f"Mutating. Best = {self.population[0].calculate_fitness()}")
        self.sort_population()
        for sudoku in self.population[10:]:
            if random.randint(0, 99) < 20:
                m_logger.info(f"Mutating. CURRENT = {sudoku.calculate_fitness()}")
                self.mutator.mutate(sudoku)
        self.sort_population()

    # mocking starting populations:
    def save_population(self, file_path: str, sudoku_base: SudokuBoard) -> None:
        list_all_population = list()
        list_all_population.append(sudoku_base.board) # base board
        list_all_population_str = list()
        list_all_population_str_full = ""
        str_empty = ""

        for i in range(0,self.population_size):
            #for j in range(0, len(self.population[i].board)):
                #list_all_population.append(self.population[i].board[j])
            list_all_population.append(self.population[i].board)

        for k in range(0, len(list_all_population)):
            str_empty = ""
            list_all_population_str.append(str_empty.join(str(list_all_population[k])))

        #print(list_all_population_str)
        list_all_population_str_full = list_all_population_str_full.join(list_all_population_str)    
        #print(list_all_population_str_full)
        #print(type(list_all_population_str_full))
        list_all_population_str_full = list_all_population_str_full.replace('[', '')
        list_all_population_str_full = list_all_population_str_full.replace(']', '')
        list_all_population_str_full = list_all_population_str_full.replace(',', '')
        list_all_population_str_full = list_all_population_str_full.replace(' ', '')
        
        list_all_population_str_full = re.sub("(.{81})", "\\1\n", list_all_population_str_full, 0, re.DOTALL)
        list_all_population_str_full = list_all_population_str_full.rstrip("\n")

        #print('List of sudoku boards (mocking starting populations):')
        #print(list_all_population_str_full)
        #print('\n')
        file = open(file_path, 'wb')
        pickle.dump(list_all_population_str_full, file)
        file.close()
        