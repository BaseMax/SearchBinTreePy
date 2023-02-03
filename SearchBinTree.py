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
