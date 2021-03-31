from input.SudokuCSVReader import SudokuCSVReader, SudokuBoard
from model.Mutator import *
from model.SudokuSolver import SudokuSolver
from utils.BoardGenerator import BoardGenerator

#base = SudokuCSVReader(r'./input/quizzes1000perRow.txt').read(1) # comment if mocking
#solver.solve(1000, 10) # comment if mocking

# mocking:
for sudoku_num in range(0, 30):
    base = SudokuCSVReader(r'./input/SudokuDatabase.csv').read_csv(sudoku_num)
    solver = SudokuSolver(base, 2000, 50, SmartDuplicatesColumnMutator())
    solver.mock_start_pops(sudoku_num)
