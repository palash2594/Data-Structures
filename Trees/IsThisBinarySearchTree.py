# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


inOrder = list()

def check_inOrder(root):
    if root is None:
        return
    check_inOrder(root.left)
    inOrder.append(root.data)
    check_inOrder(root.right)


def check_binary_search_tree_(root):
    check_inOrder(root)
    flag = 0
    for i in range(len(inOrder) - 1):
        if inOrder[i] <= inOrder[i + 1]:
            print('No')
            flag = 1
            break
    if flag == 0:
        print('Yes')




root = Node(3)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(7)

check_binary_search_tree_(root)

