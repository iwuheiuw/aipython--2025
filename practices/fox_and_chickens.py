from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True) # Just makes sure we can hash the state, i.e., use it as a key in a dictionary or set
class State:
    """Immutable description of a river bank configuration."""
    left_foxes: int
    left_chickens: int
    boat_left: bool  # True if boat on LEFT bank

    # ---------- Utility helpers ----------

    def is_goal(self) -> bool:
        """Return True when everyone is safely on the RIGHT bank."""
        # TODO: implement goal test
        ...

    def is_valid(self) -> bool:
        """Check the 'foxes never outnumber chickens' rule on BOTH banks."""
        # TODO: implement validity rule
        ...

    # ---------- Successor generation ----------

    def successors(self):
        """
        Yield all legal next states reachable by moving the boat with
        1-or-2 passengers (any mix of foxes/chickens) to the other shore.
        """
        # TODO: generate successor states
        yield from ()


# ---------- Search ----------

def search(start: State):
    """Return a list of states from start to goal, or None if unsolvable."""
    # TODO: standard search skeleton (scribes share your implementations with your classmates!)
    # Which search algorithm would be best to for this problem?
    frontier = deque()
    visited = set()
    parent = {}

    # ...

    return None  # TODO: replace


# ---------- CLI Runner ----------

if __name__ == "__main__":
    start_state = State(left_foxes=3, left_chickens=3, boat_left=True)
    path = search(start_state)
    if path:
        print(f"Solved in {len(path)-1} moves:")
        for step, s in enumerate(path):
            print(step, s)
    else:
        print("No solution found.")