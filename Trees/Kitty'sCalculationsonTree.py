# https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem

class Node:
    def __init__(self, data):
        self.data=data
        self.parent = None

# finding distance between the two nodes
def dist(a, b):
    listA = list()
    listB = list()

    nodeA = getNode(a)
    nodeB = getNode(b)

    while nodeA is not None:
        listA.append(nodeA.data)
        nodeA = nodeA.parent

    while nodeB is not None:
        listB.append(nodeB.data)
        nodeB = nodeB.parent

    if len(listA) > len(listB):
        diff = len(listA) - len(listB)
    else:
        diff = len(listB) - len(listA) # keeping bigger list in listA
        temp = listA
        listA = listB
        listB = temp

    pos = 0
    for i in range(len(listB)):
        if listB[i] == listA[diff + i]: break
        pos += 1

    return diff + pos + 1


# checks whether b in present in the nodelist
def checkNodeList(b):
    for i in range(len(nodesList)):
        if nodesList[i].data == b:
            return True

    return False

# finding node from the value
def getNode(a):
    for i in range(len(nodesList)):
        if nodesList[i].data == a:
            return nodesList[i]

# constructing the tree from inputs
def constructTree(nodesList, childrenList, n):
    for _ in range(n - 1):
        a, b = map(int, input().split())
        nodeB = Node(b)

        if not checkNodeList(b): nodesList.append(nodeB)

        childrenList[a].append(nodeB)
        nodeB.parent = getNode(a)

if __name__ == '__main__':

    nodesList = list() # stores all the nodes in this list

    n, q = map(int, input().split())
    childrenList = [list() for i in range(n + 1)] # keeps track of all the children of parents

    root = Node(1)
    nodesList.append(root)

    constructTree(nodesList, childrenList, n)

    for _ in range(q):
        num = int(input())
        if num == 1:
            print(0)
            input()
            continue
        nodes = list(map(int, input().split()))

        if num == 2:
            val = nodes[0] * nodes[1] * (dist(nodes[0], nodes[1]))
            print(val % (10 ** 9 + 7))

        else:
            sum = 0
            for i in range(len(nodes) - 1):
                for j in range(i+1, len(nodes)):
                    sum = sum + (nodes[i] * nodes[j] * dist(nodes[i], nodes[j]))

            sum = sum % (10 ** 9 + 7)

            print(sum)



"""
#    root = Node(1)

    for _ in range(n - 1):
        a, b = map(int, input().split())
 #       node = Node(b)
        childrenList[a].append(b)

    for _ in range(q):
        num = int(input())
        nodes = map(int, (input().split()))
        if len(nodes) == 1:
            print(0)
        if len(nodes) == 2:
            dist = dist(nodes[0], nodes[1], childrenList)

"""