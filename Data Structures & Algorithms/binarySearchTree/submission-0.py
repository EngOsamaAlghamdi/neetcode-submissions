class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.leftChild = None
        self.rightChild = None

class TreeMap:
    
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if self.size == 0:
            self.root = newNode
            self.size += 1
        else:
            current = self.root
            while current:
                if key == current.key:
                    current.val = val
                    return
                elif key < current.key:
                    if current.leftChild:
                        current = current.leftChild
                    else:
                        current.leftChild = newNode
                        self.size += 1
                        return
                else:
                    if current.rightChild:
                        current = current.rightChild
                    else:
                        current.rightChild = newNode
                        self.size += 1
                        return




    def get(self, key: int) -> int:
        current = self.root
        while current:
            if current.key == key:
                return current.val
            if current.key > key:
                if current.leftChild:
                    current = current.leftChild
                else:
                    return -1
            else:
                if current.rightChild:
                    current = current.rightChild
                else:
                    return -1
        return -1

    def getMin(self) -> int:
        
        if self.size == 0:
            return -1

        current = self.root
        while current.leftChild:
            current = current.leftChild
        return current.val

    def getMax(self) -> int:
        if self.size == 0:
            return -1
        
        current = self.root
        while current.rightChild:
            current = current.rightChild
        return current.val


    def remove(self, key: int) -> None:
        def deleteNode(node, target_key):
            if not node:
                return None
            
            if target_key < node.key:
                node.leftChild = deleteNode(node.leftChild, target_key)
            elif target_key > node.key:
                node.rightChild = deleteNode(node.rightChild, target_key)
            else:
                if not node.leftChild:
                    return node.rightChild
                elif not node.rightChild:
                    return node.leftChild
                
                curr = node.rightChild
                while curr.leftChild:
                    curr = curr.leftChild
                
                node.key = curr.key
                node.val = curr.val
                
                node.rightChild = deleteNode(node.rightChild, curr.key)
                
            return node
            
        self.root = deleteNode(self.root, key)


    def getInorderKeys(self) -> List[int]:
        result = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.leftChild)
            result.append(node.key)
            inorder(node.rightChild)
            
        inorder(self.root)
        return result

