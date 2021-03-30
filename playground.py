from input.SudokuCSVReader import SudokuCSVReader, SudokuBoard
from model.Mutator import *
from model.SudokuSolver import SudokuSolver
from utils.BoardGenerator import BoardGenerator

base = SudokuCSVReader(r'./input/quizzes1000perRow.txt').read(1)

solver = SudokuSolver(base, 10, 10, SmartDuplicatesColumnMutator())
solver.solve(10, 5)
