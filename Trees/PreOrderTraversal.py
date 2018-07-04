# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

class Node(object):

    def __init__(self, data=None, left_node = None, right_node = None):
        self.data = data
        self.left = left_node
        self.right = right_node

def preOrder(root):

    if root == None:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

