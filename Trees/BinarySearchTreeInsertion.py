# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

class Node:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def insert(root,val):
    if root == None: return Node(val)

    current = root
    while current is not None:
        if current.data < val and current.right is not None:
            current = current.right
        elif current.left is not None:
            current = current.left

    if current.data > val:
        current.right = Node(val)
    else:
        current.left = Node(val)

    return root