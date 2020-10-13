from DoublyLinkedList import DoublyLinkedList


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()
        self.iterQueue = iter(self.queue)

    def size(self):
        return self.queue.size

    
    def is_empty(self):
        return self.size() == 0

    
    def peek(self):
        return self.queue.peek_first()

    
    def enqueue(self, elem):
        self.queue.add_last(elem)
    

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        self.queue.remove_first()

    
    def __iter__(self):
        self.iterQueue = iter(self.queue)
        return self


    def __next__(self):
        return next(self.iterQueue)

    
    def __str__(self):
        return self.queue.__str__()


q = Queue()

q.enqueue(100)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q)

q.dequeue()
q.dequeue()
q.dequeue()
print(q)