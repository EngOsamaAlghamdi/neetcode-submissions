class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev =  None

class Deque:
    
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        if self.size == 0: return True
        else: return False

    def append(self, value: int) -> None:
        
        newNode = Node(value)           #Creating new Node

        if self.isEmpty():           
            self.head = self.tail = newNode     # the list is empty so the head and tail would be the same
        
        else:
            self.tail.next = newNode    #Add the new Node at the end of the list
            newNode.prev = self.tail      #Connect the New node with the prev Node     
            self.tail = newNode           # making the New Node the tail
        
        self.size += 1                    # Update the size for both cases

    def appendleft(self, value: int) -> None:
        
        newNode = Node(value)           #Creating new Node

        if self.isEmpty():           
            self.head = self.tail = newNode     # the list is empty so the head and tail would be the same

        else:
            newNode.next = self.head    #Add the new Node at the beginning of the list
            self.head.prev = newNode      #Connect the New node with the next Node 
            self.head = newNode           # making the New Node the head
        
        self.size += 1                    # Update the size for both cases


    def pop(self) -> int:
       
       if self.isEmpty():
            return -1

       val = self.tail.val

       if self.size == 1:
           self.head.tail = None

       else:
           self.tail = self.tail.prev
           self.tail.next.prev = None
           self.tail.next = None
        
       self.size -= 1
       return val


    def popleft(self) -> int:
        
        if self.isEmpty():
            return -1

        val = self.head.val

        if self.size == 1:
            self.head = self.tail = None
        
        else:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
        
        self.size -= 1
        return val
