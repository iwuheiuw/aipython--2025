from collections import deque
from dataclasses import dataclass
from typing import Optional, Tuple, List

# Need to define all the moves that are possible
MOVES = [
    (0, 1, 3), (0, 2, 5),
    (1, 3, 6), (1, 4, 8),
    (2, 4, 7), (2, 5, 9),
    (3, 1, 0), (3, 4, 5),
    (3, 6, 10), (3, 7, 12),
    (4, 7, 11), (4, 8, 13),
    (5, 2, 0), (5, 4, 3),
    (5, 8, 12), (5, 9, 14),
    (6, 3, 1), (6, 7, 8),
    (7, 4, 2), (7, 8, 9),
    (8, 4, 1), (8, 7, 6),
    (9, 5, 2), (9, 8, 7),
    (10, 6, 3), (10, 11, 12),
    (11, 7, 4), (11, 12, 13),
    (12, 7, 3), (12, 8, 5),
    (12, 11, 10), (12, 13, 14),
    (13, 8, 4), (13, 12, 11),
    (14, 9, 5), (14, 13, 12),
]

# We can actually handle everything by just enforcing the mirror symmetry (rotational symmetry is handled by the canonical function)
MIRROR = [0, 2, 1, 5, 4, 3, 9, 8, 7, 6, 14, 13, 12, 11, 10]


def mirror_state(state: List[bool]) -> List[bool]:
    return [state[MIRROR[i]] for i in range(15)]

# Let's just use pythons tuple comparison to handle which state is the canonical one
def canonical(state: List[bool]) -> Tuple[bool, ...]:
    a = tuple(state)
    b = tuple(mirror_state(state))
    return a if a < b else b

# We'll use this to store the nodes, the frozen dataclass makes sure we can hash the state, i.e., use it as a key in a dictionary or set
# This will also help us keep track of the path to the goal
@dataclass(frozen=True)
class Node:
    board: List[bool]
    move: Optional[Tuple[int, int, int]]
    prev: Optional["Node"]


def apply_move(board: List[bool], m: Tuple[int, int, int]) -> List[bool]:
    src, mid, dst = m
    if board[src] and board[mid] and not board[dst]:
        new_board = board.copy()
        new_board[src] = False
        new_board[mid] = False
        new_board[dst] = True
        return new_board
    return None


def bfs(start_board: List[bool]) -> Optional[Node]:
    # The frontier is the queue of nodes to explore
    frontier = deque([Node(start_board, None, None)])
    # We need to keep track of the visited states to avoid infinite loops and we'll always use the canonical form
    visited = {canonical(start_board)}

    while frontier:
        node = frontier.popleft()

        # Goal test: exactly one peg remains
        if node.board.count(True) == 1:
            return node

        # TODO: iterate over MOVES, check legality, create next boards
        #       use canonical() + visited set to avoid repeats
        #       append new Node objects to frontier
    return None 


# Pretty printing

def decode_move(m: Tuple[int, int, int]) -> str:
    return f"Move {m[0]} → {m[2]}"

def print_state(list, size):
    position = 0
    for i in range(1, size+1):
        print(" "*(size-i), end="")
        for j in range(i):
            if list[position] == 0:
                print("O ", end="")
            if list[position] == 1:
                print("# ", end="")
            position += 1
        print()


def print_solution(goal_node: Node, start_board: List[bool]):
    path: List[Tuple[int, int, int]] = []
    n = goal_node
    while n.prev is not None:
        path.append(n.move)
        n = n.prev
    path.reverse()
    
    print("Starting state:")
    print_state(canonical(start_board), 5)
   
    new_board = start_board.copy()
    for i, m in enumerate(path, 1):
        print(f"{i:02d}. {decode_move(m)} to get:")
        new_board = apply_move(new_board, m)
        if new_board is not None:
            print_state(new_board, 5)
        else:
            print("Invalid move")
    print(f"Total moves: {len(path)}")

# Runner
if __name__ == "__main__":
    start = [True] * 15
    start[0] = False

    goal = bfs(start)
    if goal:
        print_solution(goal, start)
    else:
        print("No solution found.")