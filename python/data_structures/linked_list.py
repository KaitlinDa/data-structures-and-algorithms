class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise TargetError('List is empty')

        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next is None:
            raise TargetError('Target not found in the list')

        new_node.next = current.next
        current.next = new_node

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise TargetError('List is empty')

        current = self.head
        while current and current.value != value:
            current = current.next

        if current is None:
            raise TargetError('Target not found in the list')

        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        current = self.head
        string_representation = ""
        while current:
            formatted_current_value = f"{{ {current.value} }} -> "
            string_representation += formatted_current_value
            current = current.next

        string_representation += "NULL"
        return string_representation

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("k cannot be negative")

        lead = self.head
        follow = self.head

        for _ in range(k):
            if not lead:
                raise TargetError("k is larger than the length of the list")
            lead = lead.next

        while lead and lead.next:
            follow = follow.next
            lead = lead.next

        if not lead:
            raise TargetError("k is larger than the length of the list")

        return follow.value

class TargetError(Exception):
    pass