def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None

def is_safe(grid, row, col, num):
    # Check if the number is already used in the row
    if num in grid[row]:
        return False

    # Check if the number is already used in the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if the number is already used in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    row, col = find_empty_location(grid)

    # If no empty location is found, the puzzle is solved
    if row is None:
        return True

    # Try placing numbers 1-9 in the empty location
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            # Recursively solve the rest of the puzzle
            if solve_sudoku(grid):
                return True

            # If the number doesn't lead to a solution, backtrack
            grid[row][col] = 0

    # No valid number could be placed, backtrack
    return False

# Example Sudoku puzzle (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(grid):
    print("Sudoku puzzle solved successfully:")
    print_grid(grid)
else:
    print("No solution exists for the Sudoku puzzle.")
