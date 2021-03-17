from input.SudokuCSVReader import SudokuCSVReader, SudokuBoard
from utils.BoardGenerator import BoardGenerator
from model.Crossover import *


base_sudoku = SudokuCSVReader(r'./input/quizzes1000perRow.txt').read(1)
sudoku_population = BoardGenerator(base_sudoku).generate_population(2)

for row in base_sudoku.board:
    print(row)

print('\n')

for row in sudoku_population[0].board:
    print(row)

print('\n')

for row in sudoku_population[1].board:
    print(row)

print('\n')

crossover_result = OneRowCrossover(sudoku_population[0], sudoku_population[1]).crossover()

for row in crossover_result.board:
    print(row)
