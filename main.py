import tkinter as tk
import sudoku
import requests


sudoku_instance = sudoku.Sudoku()

def get_sudoku_from_api():
    url = "https://sudoku-api.vercel.app/api/dosuku"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        value = data['newboard']['grids'][0]['value']
        solution = data['newboard']['grids'][0]['solution']
        difficulty = data['newboard']['grids'][0]['difficulty']
        return value, solution, difficulty
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

value, solution, difficulty = get_sudoku_from_api()

# Function to update the values in the GUI
def update():
    for i in range(9):
            for j in range(9):
                cell = cells[i][j]
                value = sudoku_instance.get_value(i, j)
                if value == None:
                    value = ''
                if isinstance(cell, tk.Entry):
                    cell.delete(0, tk.END)
                    cell.insert(0, str(value))
                else:
                    cell.config(text=str(value))


# Function to set the values of the cells from the GUI
def set_values():
    for i in range(9):
        for j in range(9):
            cell = cells[i][j]
            if isinstance(cell, tk.Entry):
                value = cell.get()
                if value != '':
                    sudoku_instance.set_value(i, j, int(value))
            else:
                value = cell.cget('text')
                if value != '':
                    sudoku_instance.set_value(i, j, int(value))
    update()

def solve():
    set_values()
    sudoku_instance.solve()
    update()

def clear():
    sudoku_instance.clear()
    update()

def new_game():
    sudoku_instance.clear() # We clear the values of the cells before generating a new game
    value, _, _ = get_sudoku_from_api()
    sudoku_instance.set_values_from_list(value)
    update()
    

root = tk.Tk()
root.title("Sudoku")

# Create a frame to hold the Sudoku grid
grid_frame = tk.Frame(root)
grid_frame.pack(padx=10, pady=10)

cells = []

for i in range(9):
    row = []
    for j in range(9):
        # Determine the background color of the cells so that the 3x3 blocks are detectable
        if i in [3, 4, 5] and j in [3, 4, 5]:
            color = 'gray'
        elif i in [0, 1, 2] and j in [0, 1, 2, 6, 7, 8]:
            color = 'gray'
        elif i in [6, 7, 8] and j in [0, 1, 2, 6, 7, 8]:
            color = 'gray'
        else:
            color = 'white'

        value = sudoku_instance.get_value(i, j)
        if value:
            cell = tk.Label(grid_frame, text=str(value), width=2, font=('Arial', 20), justify='center', bg=color, fg='black')
        else:
            cell = tk.Entry(grid_frame, width=2, font=('Arial', 20), justify='center',bg=color, fg='black')
            
        cell.grid(row=i, column=j)
        row.append(cell)
    cells.append(row)


# Create buttons for solving, clearing, and starting a new game
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

clear_button = tk.Button(buttonframe, text="Clear", command=clear)
clear_button.grid(row=0, column=0, padx=5, pady=5)
solve_button = tk.Button(buttonframe, text="Solve", command=solve)
solve_button.grid(row=0, column=1, padx=5, pady=5)
new_game_button = tk.Button(buttonframe, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2, padx=5, pady=5)
buttonframe.pack(padx=10, pady=10)


# Start the main event loop
root.mainloop()


