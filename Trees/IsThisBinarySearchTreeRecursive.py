# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_BST(root, minVal, maxVal):
    if root == None:
        return True

    if root.data < minVal or root.data > maxVal:
        return False

    return (check_BST(root.left,  minVal, root.data - 1) and check_BST(root.right, root.data + 1, maxVal))

def check_binary_search_tree_(root):
    return check_BST(root, 0, 10000)

root = Node(3)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(7)

print(check_binary_search_tree_(root))