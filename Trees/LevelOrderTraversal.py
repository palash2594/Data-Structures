# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

class Node:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def levelOrder(root):
    queue = []
    counter = 0
    print(root.data)
    if root.left is not None:
        queue.append(root.left)
    if root.right is not None:
        queue.append(root.right)
    while len(queue) is not 0:
        temp = queue.pop(0)
        print(temp.data)
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
