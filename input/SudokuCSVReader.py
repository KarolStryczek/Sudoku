from model.SudokuBoard import SudokuBoard
from typing import List
import csv
import pickle


class SudokuCSVReader:
    def __init__(self, file_path: str, read_mock: bool) -> None:
        #self.file = open(file_path, 'r') # comment if mocking
        if read_mock:
            self.file = open(file_path, 'rb')
        else:
            self.file = open(file_path, 'r', newline = '') # mock
        self.current_row = 0

    def read(self, sudoku_number: int) -> SudokuBoard:
        sudoku_string = None
        while self.current_row < sudoku_number:
            sudoku_string = self.file.readline()
            self.current_row += 1
            
        return SudokuBoard(sudoku_string.strip())

    def read_from_mock(self, population_size: int) -> List[SudokuBoard]:
        sudoku_board_list = list()
        sudoku_string = pickle.load(self.file).splitlines()
        while self.current_row <= population_size:
            sudoku_board_list.append(sudoku_string[self.current_row])
            self.current_row += 1
        return sudoku_board_list

    # mocking starting populations:
    def read_csv(self, sudoku_number: int) -> SudokuBoard:
        sudoku_string = None
        sudoku_string_line = None
        sudoku_string = csv.reader(self.file)
        sudoku_string_line = list(sudoku_string)
        return SudokuBoard(sudoku_string_line[sudoku_number][0])

    def __del__(self) -> None:
        self.file.close()
