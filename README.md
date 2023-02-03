# Search Bin-Tree Python

A simple python class for search in binary tree. This class provides a few methods for searching in binary tree. Search methods are recursive and non-recursive. You can easily search in binary tree with only on left or right child, and you can search in binary tree with both left and right child.

## Example

```python
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
```

Copyright (c) 2023, Max Base
