from model.SudokuBoard import SudokuBoard
import csv


class SudokuCSVReader:
    def __init__(self, file_path: str) -> None:
        #self.file = open(file_path, 'r') # comment if mocking
        self.file = open(file_path, 'r', newline = '') # mock
        self.current_row = 0

    def read(self, sudoku_number):
        sudoku_string = None
        while self.current_row < sudoku_number:
            sudoku_string = self.file.readline()
            self.current_row += 1
            
        return SudokuBoard(sudoku_string.strip())

    # mocking starting populations:
    def read_csv(self, sudoku_number: int):
        sudoku_string = None
        sudoku_string_line = None
        sudoku_string = csv.reader(self.file)
        sudoku_string_line = list(sudoku_string)
        #print('A read board:')
        #print(sudoku_string_line[sudoku_number][0])
        #print('\n')
        return SudokuBoard(sudoku_string_line[sudoku_number][0])

    def __del__(self) -> None:
        self.file.close()
