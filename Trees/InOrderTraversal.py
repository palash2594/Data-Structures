# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem

class Node(object):

    def __init__(self, data=None, left_node = None, right_node = None):
        self.data = data
        self.left = left_node
        self.right = right_node

def inOrder(root):

    if root == None:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)