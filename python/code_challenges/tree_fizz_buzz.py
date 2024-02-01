from data_structures.binary_tree import BinaryTree


class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []  

class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        """A method to return the values of the tree nodes in breadth-first order."""
        values = []
        queue = [self.root] if self.root else []

        while queue:
            current = queue.pop(0)
            values.append(str(current.value))
            for child in current.children:
                queue.append(child)

        return values

def fizz_buzz(value):
    """Helper function to transform the value based on divisibility."""
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return str(value)

def fizz_buzz_tree(kary_tree):
    """Transforms the k-ary tree values based on the FizzBuzz rules."""
    def clone_tree(node):
        if node is None:
            return None
        new_node = Node(fizz_buzz(node.value))
        new_node.children = [clone_tree(child) for child in node.children]
        return new_node

    return KaryTree(clone_tree(kary_tree.root))

