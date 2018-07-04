# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

def displayInOrder(root):
    if root == None:
        return
    displayInOrder(root.left)
    print(root.data, end = ' ')
    displayInOrder(root.right)

def constructTree(indexes):
    root = Node(1)
    queue = list()
    queue.append(root)
    for item in indexes:
        temp = queue.pop(0)
        if item[0] != -1:
            temp.left = Node(item[0])
            queue.append((temp.left))
        if item[1] != -1:
            temp.right = Node(item[1])
            queue.append((temp.right))

    return root

def fillList(toSwapList):
    notToSwapList = list()
    while len(toSwapList) != 0:
        node = toSwapList.pop(0)
        if node.left != None:
            notToSwapList.append(node.left)
        if node.right != None:
            notToSwapList.append(node.right)
    return notToSwapList

def swapList(toSwapList):
    for i in range(len(toSwapList)):
        node = toSwapList.pop(i)
        toSwapList.insert(i, node)
        if node.left == None and node.right == None:
            continue
        elif node.left != None and node.right == None:
            node.right = node.left
            node.left = None
        elif node.left == None and node.right != None:
            node.left = node.right
            node.right = None
        elif node.left != None and node.right != None:
            temp = node.right
            node.right = node.left
            node.left = temp

def swapNodes(indexes, queries):
    root = constructTree(indexes)
    displayInOrder(root)
    print()
    toSwapList = list()
    notToSwapList = list()
    for item in queries:
        height = 0
        notToSwapList.append(root)
        while len(notToSwapList)!= 0 or len(toSwapList) != 0:
            height += 1
            if height % item == 0:
                while len(notToSwapList) != 0:
                    node = notToSwapList.pop(0)
                    toSwapList.append(node)
                dupeSwapList = toSwapList
                swapList(dupeSwapList)
                notToSwapList = fillList(toSwapList) # fills elements from swapList to notSwapList
            else:
                leng = len(notToSwapList)
                while leng != 0:
                    node = notToSwapList.pop(0)
                    if node.left != None: notToSwapList.append(node.left)
                    if node.right != None: notToSwapList.append(node.right)
                    leng -= 1

        displayInOrder(root)
        print()

if __name__ == '__main__':

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries.append(int(input()))

    result = swapNodes(indexes, queries)
