from input.SudokuCSVReader import SudokuCSVReader
from model.Mutator import *
from model.SudokuSolver import SudokuSolver

do_mocking_start_pop = False
do_read_from_mocking_start_pop = True
chosen_sudoku_board = 29
population_size = 300
cross_per_iter = 300
max_iter = 500
max_no_improve = 10
mutator = RandomInRowMutator()

if do_mocking_start_pop:
    do_read_from_mocking_start_pop = False
    read_mock = False
    # mocking:
    for sudoku_num in range(0, 30):
        base = SudokuCSVReader(r'./input/SudokuDatabase.csv', read_mock).read_csv(sudoku_num)
        solver = SudokuSolver(base, population_size, cross_per_iter, mutator)
        solver.create_start_population()
        solver.mock_start_pops(sudoku_num)
else:
    if do_read_from_mocking_start_pop:
        read_mock = True
        # reading mocked:
        base = SudokuCSVReader(rf'./input/mocking_start_pops/mock_start_{chosen_sudoku_board}.pkl', read_mock).read_from_mock(population_size)
        solver = SudokuSolver(SudokuBoard(base[0]), population_size, cross_per_iter, mutator)
        board_list = list()
        for board_elem in range (1, len(base)):
            board_list.append(SudokuBoard(base[board_elem]))

        solver.read_mock_start_pops(board_list)
        
    else:
        # normal mode:
        read_mock = False
        base = SudokuCSVReader(r'./input/quizzes1000perRow.txt', read_mock).read(chosen_sudoku_board)
        solver = SudokuSolver(base, population_size, cross_per_iter, mutator)
        solver.create_start_population()

    solver.solve(max_iter, max_no_improve)