

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

"""
def addNode(lastNode, newNode):
    lastNode.next = newNode
"""

def Reverse(head):
    prev = None
    cur = head
    nxt = cur.next

    while cur is not None:
        nxt = cur.next
        cur.nxt = prev
        prev = cur
        cur = nxt

    head = prev
    return head

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