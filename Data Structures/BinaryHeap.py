class BinaryHeap:
    def __init__(self) -> None:
        self.heapList = [0]
        self.size = 0

    def bubble_up(self, i):
        """Move an item up the priority queue if its smaller
        than the element above.
        """
        while i // 2 > 0:
            if self.healList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2
    
    def insert(self, k):
        """Insert element at the end of the queue

        Args:
            k (Any comparable type): Element to be inserted
        """ 
        self.heapList.append(k)  # Add item to first empty position
        self.size += 1
        self.bubble_up(self.size)
 
    def bubble_down(self, i):
        """Move an element down the queue until it finds
        the correct position
        """
        while (i * 2) <= self.size:
            mc = self.minimum_child(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc 

    def minimum_child(self, i):
        """Find the minimum child of a node
        """
        if (i * 2 + 1) > self.size:
            return i * 2 
        else:
            if self.heapList[i*2] < self.heapList[i+2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_minimum(self):
        """Retrieve the element with the highest priority

        Returns:
            element: element with highest priority
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.bubble_down(1)
        return retval

    def heapify(self, lst):
        """Build a heap from a list
        """
        i = len(lst) // 2
        self.size = len(lst)
        self.heapList = [0] + lst[:]
        while i > 0:
            self.bubble_down(i)
            i = i - 1
