import random
import string

charecters = list(string.ascii_lowercase)

class Node:
    def __init__(self, name=str, parent=None, cost=float):
        self.name = name
        self.parent = parent
        self.cost = cost

    def __str__(self):
        parent_name = self.parent.name if self.parent else "None"
        return f"Node(name={self.name}, parent={parent_name}, cost={self.cost:.3f})"

    def __repr__(self):
        return self.__str__()


# Build nodes with random cost and linked parent structure
for i in range(len(charecters)):
    if i != 0:
        charecters[i] = Node(charecters[i], charecters[i-1], cost=random.uniform(0, 1))
    else:
        charecters[i] = Node(charecters[i], cost=random.uniform(0, 1))

# Find node(s) with largest cost
largest = 0.0
char = []
for node in charecters:
    if node.cost > largest:
        largest = node.cost
        char = [node.name]
    elif node.cost == largest:
        char.append(node.name)

print("Node(s) with largest cost:", char, f"(cost: {largest:.3f})")

# Get path from a node to root
def get_path(node):
    path = []
    total_cost = 0
    while node:
        path.append(node.name)
        total_cost += node.cost
        node = node.parent
    path.reverse()
    print(" -> ".join(path))
    print(f"Total cost: {total_cost:.3f}")

# Call it on 'z'
get_path(charecters[25])
