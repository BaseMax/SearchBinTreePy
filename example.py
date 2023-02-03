from SearchBinTree import *

# Create tree
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
