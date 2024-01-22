from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    """
    A Stack implementation using a linked list.
    Each Stack instance has a top attribute which points to the top of the stack.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Pushes a new value onto the top of the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Pops the top value from the stack and returns it.
        Raises InvalidOperationError if the stack is empty.
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        pop_value = self.top.value
        self.top = self.top.next
        return pop_value

    def peek(self):
        """
        Returns the value at the top of the stack without removing it.
        Raises InvalidOperationError if the stack is empty.
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return self.top is None
