class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size < len(self.array):
            self.array[self.size] = n
            self.size += 1
        else:
            self.resize()
            self.pushback(n)


    def popback(self) -> int:
        n = self.array[self.size - 1]
        self.size -= 1
        return n

    def resize(self) -> None:
        doubled_sized_array = [None] * (len(self.array) * 2)
        i = 0
        while i < self.size:
            doubled_sized_array[i] = self.array[i]
            i += 1
        self.array = doubled_sized_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.array)