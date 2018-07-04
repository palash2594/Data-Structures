# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

def findNode(root, val):
    list = []

    while root is not None:
        list.append(root)
        if root.data == val:
            return list
        else:
            if root.data > val:
                root = root.right
            else: root = root.left
    return list

def lca(root , v1 , v2):

    listV1 = findNode(root, v1)
    listV2 = findNode(root, v2)

    if len(listV1) > len(listV2):
        diff = len(listV1) - len(listV2)
        bigList = listV1
        smallList = listV2
    else:
        diff = len(listV2) - len(listV1)
        bigList = listV2
        smallList = listV1

    for i in range(len(bigList) - diff - 1, -1, -1):
        if smallList[i] == bigList[i]:
            print(smallList[i].data)
            return smallList[i]