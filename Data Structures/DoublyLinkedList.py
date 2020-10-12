class DoublyLinkedList:
    """Doubly Linked List implementation

    Returns:
        DoublyLinkedList
    """
    class Node:
        """Inner node classes used to create
        individual nodes for the Doubly Linked List
        """        
        def __init__(self, data, prev, nxt):
            """Constructor of each node

            Args:
                data : An object to be held
                prev : Reference to previous node
                nxt : Reference to next node
            """            
            self.data = data
            self.prev = prev
            self.nxt = nxt
        

    def __repr__(self):
        """Convert Node to string

        Returns:
            str: Node data
        """
        return str(self.data)


    def __init__(self):
        """Constructor
        """
        self.size = 0
        self.head = None
        self.tail = None
        self.travIter = None


    def clear(self):
        """Empty the linked list O(n)
        """
        trav = self.head
        while trav is not None:
            nxt = trav.nxt
            trav.prev = trav.nxt
            trav.data = None
            trav = nxt


        self.head = None
        self.tail = None
        trav = None
        self.size = 0
    

    def __len__(self): 
        """ 
        Return number of elements sorted in array 
        """
        return self.llSize


    def size(self):
        """Return the size of linked list

        Returns:
            int: Linked list size
        """
        return self.size


    def is_empty(self):
        """Check if the list is empty

        Returns:
            bool: Comapres size to 0
        """
        return self.size == 0


    def add(self, elem):
        """Add an element to the linked list using add_last

        Args:
            elem (object): Any type of object to be added
        """
        self.add_last(elem)

    
    def add_first(self, elem):
        """Add element to the front of the linked list

        Args:
            elem (object): Any type of object to be added
        """
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, None, self.head)
            self.head = self.head.prev
        
        self.size += 1

    
    def add_last(self, elem):
        """Add to the end of the Linked list by append to
        tail.next O(n)

        Args:
            elem (object): Any type of object to be added
        """
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.nxt = Node(elem, self.tail, None)
            self.tail = self.tail.nxt

        self.size += 1

    
    def peek_first(self):
        """Obtain data from head of linked list O(1)

        Raises:
            RuntimeError: Empty list

        Returns:
            object: Data held in head Node
        """
        if self.is_empty(): raise RuntimeError("Empty list")
        return self.head.data


    def peek_last(self):
        """Obtain data from tail of linked list  O(1)

        Raises:
            RuntimeError: Empty list

        Returns:
            Object: Data held in tail Node
        """
        if self.is_empty(): raise RuntimeError("Empty list")
        return self.tail.data

    
    def remove_first(self):
        """Remove Node at the head of the linked list O(1)

        Raises:
            RuntimeError: Empty list

        Returns:
            Object: Data of the removed node
        """
        if self.is_empty(): raise RuntimeError("Empty list")

        data = self.head.data
        self.head = self.head.nxt
        self.size -= 1

        if self.is_empty(): self.tail = None
        else: self.head.prev = None

        return data


    def remove_last(self):
        if self.is_empty(): raise RuntimeError("Empty list")

        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1

        if self.is_empty(): self.head = None
        else: self.tail.nxt = None

        return data

    
    def __remove__(self, node):
        if node.prev == None: return self.remove_first()
        if node.nxt == None: return self.remove_last()

        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt

        data = node.data

        node.data = None
        node.nxt = None
        node.prev = None
        node = None

        self.size -= 1

        return data

    
    def remove_at(self, index):
        if index < 0 or index >= size: raise ValueError("Wrong index")

        i = 0
        trav = None

        if index < self.size / 2:
            trav = self.head
            while i != index:
                i += 1
                trav= trav.nxt
            
        else:
            i = self.size
            trav = self.tail
            while i != index:
                i -= 1
                trav = trav.prev

        
        return self.__remove__(trav)

    
    def remove(self, obj):
        
        trav = self.head

        if obj == None:
            while trav is not None:
                if trav.data is None:
                    self.__remove__(trav)
                    return True

                trav = trav.nxt
        
        else:
            trav = self.head

            while trav is not None:
                if obj == trav.data:
                    self.__remove__(trav)
                    return True

                trav = trav.nxt

        return False

        
    def index_of(self, obj):
        index = 0
        trav = self.head

        if obj is None:
            while trav is not None:
                if trav.data is None:
                    return index
                trav = trav.nxt
                index += 1
        else:
            while trav is not None:
                if trav.data == obj:
                    return index
                trav = trav.nxt
                index += 1
        
        return -1


    def contains(self, obj):
        return self.index_of(obj) != -1

    
    def __iter__(self):
        self.travIter = self.head
        return self

        
    def __next__(self):
        if self.travIter is None:
            raise StopIteration

        data = self.travIter.data
        self.travIter = self.travIter.nxt

        return data

    
    def __str__(self):
        sb = ""
        sb = sb + '[ '
        trav = self.head
        while trav is not None:
            sb = sb + str(trav.data)
            if trav.nxt is not None:
                sb = sb + ', '

            trav = trav.nxt

        sb = sb + ' ]'

        return sb
