class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
            if index >= self.size:
                return -1
            current = self.head
            i = 0

            while i < index:
                current = current.next
                i += 1
            return current.data

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        if self.size == 1:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.size != 0 :
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.tail = self.head = newNode
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size or self.size == 0: #out of the boundry or the list is empty
            return False

        if self.size == 1:
            self.head = self.tail = None        # The list has one item
            self.size = 0
            return True

        if index == 0:
            self.head = self.head.next               # Delete the first item
            self.size -= 1
            return True
        
        i = 0
        current = self.head
        prev = None
        while i < index:
            prev = current
            current = current.next
            i += 1
        prev.next = current.next
        if current == self.tail:
            self.tail = prev
        current.next = None
        self.size -= 1
        return True
            



    def getValues(self) -> List[int]:
        array = []

        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

