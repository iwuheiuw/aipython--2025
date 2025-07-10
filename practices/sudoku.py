from collections import deque
import copy

# Create cell names like A1, A2, ..., I9
rows = "ABCDEFGHI"
cols = "123456789"
cells = [r + c for r in rows for c in cols]

# Helper to get peers (cells in the same row/col/box)
def get_neighbors():
    units = []

    for r in rows:
        units.append([r + c for c in cols])
    for c in cols:
        units.append([r + c for r in rows])
    for rs in ("ABC", "DEF", "GHI"):
        for cs in ("123", "456", "789"):
            units.append([r + c for r in rs for c in cs])

    neighbors = {cell: set() for cell in cells}
    for unit in units:
        for cell in unit:
            neighbors[cell].update(set(unit) - {cell})
    return neighbors

neighbors = get_neighbors()

# Initial domains: use provided board or all digits
def create_domains(sudoku_board):
    domains = {}
    for i, cell in enumerate(cells):
        row = i // 9
        col = i % 9
        val = sudoku_board[row][col]
        if val == 0:
            domains[cell] = set("123456789")
        else:
            domains[cell] = set(str(val))
    return domains

# AC-3 Algorithm
def AC3(start_node, domains):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        for neighbor in neighbors[node]:
            new_domain = enforce_arc_consistency(neighbor, node, domains)
            if new_domain != domains[neighbor]:
                domains[neighbor] = new_domain
                queue.append(neighbor)
    return domains

# Enforce arc consistency: remove values from Xi that conflict with Xj
def enforce_arc_consistency(Xi, Xj, domains):
    revised_domain = set()
    for x in domains[Xi]:
        if any(x != y for y in domains[Xj]):
            revised_domain.add(x)
    return revised_domain

# Display Sudoku board
def print_sudoku(domains):
    for r in rows:
        if r in "DEF":
            print("-" * 21)
        row = ""
        for c in cols:
            if c in "456":
                row += "| "
            val = domains[r + c]
            row += (next(iter(val)) if len(val) == 1 else ".") + " "
        print(row)

# Example Sudoku board (0 = blank)
sudoku_board = [
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

# Setup and run AC-3
domains = create_domains(sudoku_board)
for cell in cells:
    domains = AC3(cell, domains)

# Print final result
print_sudoku(domains)
