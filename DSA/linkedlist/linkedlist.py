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
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
    def remove(self, value): 
        if self.head is None:
            return None
        else:
            if self.head.value == value:
                self.head = self.head.next
            else:
                current = self.head
                while current.next is not None:
                    if current.next.value == value:
                        current.next = current.next.next
                        break
                    current = current.next
    
    def traverse(self, head):
        if head is None: 
            return None
        print(f"{head.value} ->")
        self.traverse(head.next)



    def __iter__(self):
        """Iterate over the list"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

if __name__ == "__main__":
    List = LinkedList()
    List.add(1)
    List.add(2)
    List.add(3)
    List.add(4)

    List.traverse(List.head)

    List.remove(3)

    List.traverse(List.head)