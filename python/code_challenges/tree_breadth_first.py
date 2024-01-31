from data_structures.binary_tree import BinaryTree

from collections import deque

def breadth_first(tree):
    if not tree.root:
        return []

    queue = deque([tree.root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result
