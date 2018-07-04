# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem

class Node(object):

    def __init__(self, data=None, left_node = None, right_node = None):
        self.data = data
        self.left = left_node
        self.right = right_node

def postOrder(root):

    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)