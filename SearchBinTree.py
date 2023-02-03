# 
# 2023-02-03
# Max Base
# https://github.com/BaseMax/SearchBinTreePy
#

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" ")
        if self.right:
            self.right.PrintTree()

    def searchData(self, data):
        if data < self.data:
            if self.left is None:
                return -1
            return self.left.searchData(data)
        elif data > self.data:
            if self.right is None:
                return -1
            return self.right.searchData(data)
        else:
            return self.data
    
    def searchLeftData(self, data):
        if data < self.data:
            if self.left is None:
                return -1
            return self.left.searchLeftData(data)
        elif data > self.data:
            if self.right is None:
                return -1
            return self.right.searchLeftData(data)
        else:
            return self.data
    
    def searchRightData(self, data):
        if data < self.data:
            if self.left is None:
                return -1
            return self.left.searchRightData(data)
        elif data > self.data:
            if self.right is None:
                return -1
            return self.right.searchRightData(data)
        else:
            return self.data
    
    def searchDataNonRecursive(self, data):
        while self is not None:
            if data < self.data:
                self = self.left
            elif data > self.data:
                self = self.right
            else:
                return self.data
        return -1

root = Node(12)
root.left = Node(6)
root.right = Node(14)
root.left.left = Node(3)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(15)

print("Tree:")
root.PrintTree()
print("")

print("Test searchData:")
print(root.searchData(9))
print(root.searchData(10))

print("Test searchDataNonRecursive:")
print(root.searchDataNonRecursive(9))
print(root.searchDataNonRecursive(10))

print("Test searchLeftData:")
print(root.searchLeftData(9))
print(root.searchLeftData(10))

print("Test searchRightData:")
print(root.searchRightData(9))
print(root.searchRightData(10))
