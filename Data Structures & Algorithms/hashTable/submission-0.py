class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.hashTabel = [None] * capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        index = key % self.getCapacity()
        
        if self.hashTabel[index] is None:
            self.hashTabel[index] = Node(key, value)
            self.size += 1
        else:
            current = self.hashTabel[index]
            while True:
                if current.key == key:
                    current.val = value
                    return
                if current.next is None:
                    break
                current = current.next
            
            # التعديل هنا: الإضافة تكون برا اللوب
            current.next = Node(key, value)
            self.size += 1
            
        loadFactor = self.getSize() / self.getCapacity()
        if loadFactor >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.getCapacity()
        current = self.hashTabel[index]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.getCapacity()
        current = self.hashTabel[index]
        prev = None
        
        if current is None:
            return False

        while current and current.key != key:
            prev = current
            current = current.next

        if current is None:
            return False

        if prev is None:
            self.hashTabel[index] = current.next
        else:
            prev.next = current.next

        self.size -= 1
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return len(self.hashTabel)

    def resize(self) -> None:
        oldHashTabel = self.hashTabel
        newCapacity = self.getCapacity() * 2
        self.hashTabel = [None] * newCapacity

        self.size = 0

        for node in oldHashTabel:
            current = node
            while current:
                self.insert(current.key, current.val)
                current = current.next