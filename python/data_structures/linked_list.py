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

    def __str__(self):

        current = self.head

        string_representation = ""

        while current:
            formatted_current_value = f"{{ {current.value} }} -> "
            string_representation += formatted_current_value
            current = current.next

        string_representation += "NULL"
        
        return string_representation
    
class TargetError:
    pass