# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

"""
def addNode(lastNode, newNode):
    lastNode.next = newNode
"""

def Reverse(head):
    newHead = None
    while head is not None:
        newNode = Node(head.data, newHead)
        newHead = newNode
        head = head.next

    return newHead

def display(head):
    while head is not None:
        print(head.data)
        head = head.next

node = Node(1)
node1 = Node(2, node)
node2 = Node(3, node1)
node3 = Node(4, node2)
node4 = Node(5, node3)
node5 = Node(6, node4)
node6 = Node(7, node5)

#display(node6)
#print('Break')

display(Reverse(node6))

"""
for i in range(7):
    print(node6.data)
    node6 = node6.next
"""

"""
    list = []
    while head is not None:
        list.append(head.data)
        head = head.next
    lastNode = Node(list[len(list) - 1])
    head = lastNode
    for i in range(list.size() - 1, -1, -1):
        newNode = Node(list[i])
        addNode(lastNode, newNode)
        lastNode = lastNode.next
    return lastNode
"""