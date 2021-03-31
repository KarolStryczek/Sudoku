from input.SudokuCSVReader import SudokuCSVReader, SudokuBoard
from model.Mutator import *
from model.SudokuSolver import SudokuSolver
from utils.BoardGenerator import BoardGenerator

#base = SudokuCSVReader(r'./input/quizzes1000perRow.txt').read(1) # comment if mocking
base = SudokuCSVReader(r'./input/SudokuDatabase.csv').read_csv(0) # mock

solver = SudokuSolver(base, 100, 50, SmartDuplicatesColumnMutator())
solver.mock_start_pops() # mock
#solver.solve(1000, 10) # comment if mocking