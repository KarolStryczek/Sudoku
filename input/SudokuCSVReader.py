from model.SudokuBoard import SudokuBoard
import csv


class SudokuCSVReader:
    def __init__(self, file_path: str) -> None:
        #self.file = open(file_path, 'r')
        self.file = open(file_path, 'r', newline = '') # mock
        self.current_row = 0

    def read(self, sudoku_number):
        sudoku_string = None
        while self.current_row < sudoku_number:
            #sudoku_string = self.file.readline()
            sudoku_string = csv.reader(self.file) # mock
            sudoku_string_line = list(sudoku_string) # mock
            self.current_row += 1
            print(sudoku_string_line[self.current_row][0]) # mock
        #return SudokuBoard(sudoku_string.strip())
        return SudokuBoard(sudoku_string_line[self.current_row][0]) # mock

    def __del__(self) -> None:
        self.file.close()
