from typing import List
import itertools


class SudokuBoard:
    def __init__(self, board_string: str = None) -> None:
        if board_string is not None:
            if len(board_string) == 81:
                self.board = [[int(board_string[i*9+j]) for j in range(0, 9)] for i in range(0, 9)]
            else:
                raise Exception("Sudoku should have 81 fields")
        else:
            self.board = [[0 for j in range(0, 9)] for i in range(0, 9)]

    def __eq__(self, other: 'SudokuBoard') -> bool:
        for i in range(0, 9):
            for j in range(0, 9):
                if self.element(i, j) != other.element(i, j):
                    return False
        return True

    def __str__(self):
        return str(self.board)

    def __repr__(self):
        return repr(self.board)

    def element(self, row: int, col: int) -> int:
        return self.board[row][col]

    def row(self, row: int) -> List[int]:
        return self.board[row]

    def column(self, col: int) -> List[int]:
        return [self.board[i][col] for i in range(len(self.board))]

    def square(self, square_number: int) -> List[int]:
        squares = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = [item for sublist in list(itertools.chain(row[j:j+3] for row in self.board[i:i+3])) for item in sublist]
                squares.append(square)
        return squares[square_number]

    def set_element(self, row_index: int, col_index: int, number: int) -> None:
        self.board[row_index][col_index] = number

    def set_row(self, row_index: int, row: List[int]) -> None:
        if len(row) != 9:
            raise Exception("Provided row has wrong length (should be 9 digits)")
        self.board[row_index] = row

    def count_duplicates(self, checklist: List[int]) -> int:
        return len(checklist)-len(set(checklist))

    def calculate_fitness(self) -> int:
        duplicates_in_rows, duplicates_in_columns, duplicates_in_squares = 0, 0, 0
        for i in range(0,9):
            duplicates_in_rows += self.count_duplicates(self.row(i))
            duplicates_in_columns += self.count_duplicates(self.column(i))
            duplicates_in_squares += self.count_duplicates(self.square(i))
        return duplicates_in_rows + duplicates_in_columns + duplicates_in_squares
        