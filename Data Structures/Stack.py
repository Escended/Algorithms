from DoublyLinkedList import DoublyLinkedList

class Stack:
    """Stack implementation using my DoublyLinkedList
    implementation.
    """


    def __init__(self):
        """Initialise an empy ll
        """
        self.iterStack = iter(self.Stack)
        self.list = DoublyLinkedList()

    
    def size(self):
        return self.list.size

    
    def is_empty(self):
        return self.size() == 0


    def push(self, elem):
        self.list.add_last(elem)

    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is already empty")
        return self.list.remove_last()


    def peek(self):
        """Peek the last element in a stack
        as we cannot peek the top element

        Raises:
            ValueError: If the stack is empty we don't peek

        Returns:
            Node: Data store in the node 
        """
        if self.is_empty():
            raise ValueError
        return self.list.peek_last()

    
    def __iter__(self):
        self.iterStack = iter(self.stack)
        return self


    def __next__(self):
        return next(self.iterStack)

    
    def __str__(self):
        return self.list.__str__()