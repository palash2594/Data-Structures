# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

class Node:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def preOrder(root, max, count):
    count += 1
    if root == None and max < count:
        return count - 1
    max1 = preOrder(root.left, max, count)
    max2 = preOrder(root.right, max, count)

    if max1 > max2:
        return max1
    else: return max2

def height(root):
    max = 0
    count = -1
    return(preOrder(root, max, count))