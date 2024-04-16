# * Sudoku Solver *
This is a Python package for solving Sudoku puzzles.

# Overview 
This package provides classes for representing Sudoku grids and solving Sudoku puzzles programmatically.
It includes a Cell class representing individual cells in a Sudoku grid, and a Sudoku class representing the entire grid.
The solver is implemented using a * backtracking algorithm * .

# Installation
To use this package, you can simply clone the repository:
git clone https://github.com/your-username/sudoku-solver.git

# Usage
Here's a basic example demonstrating how to use the Sudoku solver:
'''
from sudoku_solver import Sudoku

# Create a Sudoku instance
puzzle = Sudoku()

# Set values from a string representation of the puzzle
puzzle.set_values_from_string("530070000600195000098000060800060003400803001700020006060000280000419005000080079")

# Solve the puzzle
puzzle.solve()

# Print the solved grid
puzzle.print_grid()
'''
