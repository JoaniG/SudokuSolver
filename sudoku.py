from dataclasses import dataclass, field
from typing import List


@dataclass
class Cell:
    row: int
    column: int
    block: int = None
    value: int = None

    def __post_init__(self):
        self.block = (self.row // 3) * 3 + (self.column // 3)
        

    def set_value(self, value: int):
        self.value = value

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    
        


@dataclass(frozen=True)
class Sudoku:
    grid: List[Cell] = field(default_factory=lambda: [Cell(row, column) for row in range(9) for column in range(9)])

    def solve(self):
        def find_empty_cell():
            for cell in self.grid:
                if cell.value is None:
                    return cell
            return None

        def is_valid(cell, value):
            for c in self.grid:
                if c.row == cell.row and c.value == value and c != cell:
                    return False
                if c.column == cell.column and c.value == value and c != cell:
                    return False
                if c.block == cell.block and c.value == value and c != cell:
                    return False

            return True

        def solve_helper():
            empty_cell = find_empty_cell()
            if empty_cell is None:
                return True

            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if is_valid(empty_cell, value):
                    empty_cell.value = value
                    if solve_helper():
                        return True
                    empty_cell.value = None

            return False

        solve_helper()

    def clear(self):
        for cell in self.grid:
            cell.value = None

    def print_grid(self):
        # prints the sudoku grid
        for row in range(9):
            if row % 3 == 0:
                print("-" * 22)
            for column in range(9):
                if column % 3 == 0:
                    print("|", end="")
                if self.grid[row * 9 + column].value:
                    print(f" {self.grid[row * 9 + column].value} ", end="")
                else:
                    print(" . ", end="")
            print("|")
        print("-" * 22)




    def set_value(self, row: int, column: int, value: int):
        cell = self.grid[row * 9 + column]
        cell.set_value(value)

    
    def set_values_from_string(self, value_string):
        for i in range(len(value_string)):
            cell = self.grid[i]
            ch = value_string[i]
            if ch == ' ':
                continue
            value = int(value_string[i])
            cell.set_value(value)

    def set_values_from_list(self, value_list):
        for i in range(9):
            for j in range(9):
                cell = self.grid[i*9 + j]
                value = value_list[i][j]
                if value == 0:
                    continue
                cell.set_value(value)

    def get_value(self, row: int, column: int) -> int:
        return self.grid[row * 9 + column].value

    

