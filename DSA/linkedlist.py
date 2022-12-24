class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        """Add a new node to the end of the list"""
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            # look at how we assign tail.next to a new Node object
            # it has both the head (set to the value) and next which is none

            # thus explains how we get none at the tail
            self.tail.next = Node(value)
            self.tail = self.tail.next

    
    def __iter__(self):
        """Iterate over the list"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next



class Stack: 
    """FILO"""
    def __init__(self):
        
        self.head = None
        self.tail = None

    def pop(self):
        """Remove the last item and return its value"""
        if self.head is None:
            return None
        else:
            current = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            return current.value

    def push(self, value):
        """Add an item to the end of the list"""
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


class Queue: 
    """FIFO"""
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
    
    def pop(self):
        """Remove first value, so the root"""

        if self.head is None:
            return None
        else:
            current = self.head
            self.head = self.head.next
            return current.value

    def push(self, value):
        """Add an item to the end of the list"""
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
    


    
