from input.SudokuCSVReader import SudokuCSVReader
from utils.BoardGenerator import BoardGenerator

sudoku = SudokuCSVReader(r'./input/quizzes1000perRow.txt').read(1)
sudoku_population = BoardGenerator(sudoku).generate_population(1)

for row in sudoku.board:
    print(row)

print('\n')

for row in sudoku_population[0].board:
    print(row)

