# https://www.hackerrank.com/challenges/tree-top-view/problem

class Node:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def topView(root):
    if root == None:
        return
    print(root.data)
    topView(root.left)
    topView(root.right)