from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    A Queue implementation using a linked list.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Adds a new element with the given value to the rear of the queue.
        """
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError("Cannot dequeue from an empty queue.")

        dequeue_value = self.front.value

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return dequeue_value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Cannot peek on an empty queue.")
        return self.front.value

    def is_empty(self):
        return self.front is None