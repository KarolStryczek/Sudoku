from model.SudokuBoard import SudokuBoard


class SudokuCSVReader:
    def __init__(self, file_path: str) -> None:
        self.file = open(file_path, 'r')
        self.current_row = 0

    def read(self, sudoku_number):
        sudoku_string = None
        while self.current_row < sudoku_number:
            sudoku_string = self.file.readline()
            self.current_row += 1
        return SudokuBoard(sudoku_string.strip())

    def __del__(self) -> None:
        self.file.close()
