from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_a, tree_b):
    def traverse_and_collect_values(tree):
        values = set()
        def traverse(node):
            if node:
                values.add(node.value)
                traverse(node.left)
                traverse(node.right)
        traverse(tree.root)
        return values
    
    values_tree_a = traverse_and_collect_values(tree_a)
    values_tree_b = traverse_and_collect_values(tree_b)
    
    intersection = values_tree_a.intersection(values_tree_b)
    
    return list(intersection)
