# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

class Node(object):
    def __init__(self, data=None, next_node=None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def display(head):
    while head is not None:
        print(head.data)
        head = head.next

def SortedInsert(head, data):
    if head.data is None:
        return Node(data)
    start = head

    newNode = Node(data)
    while head is not None:
        if head.data < data:
            if head.next is None:
                head.next = newNode
                newNode.prev = head
                return head
            head = head.next
            continue

        if head.prev is None:
            newNode.next = head
            return newNode

        head.prev.next = newNode
        newNode.prev = head.prev
        newNode.next = head
        head.prev = newNode

    return start

print('Hi')
node = Node()
newHead = SortedInsert(node, 2)
#display(newHead)
newHead = SortedInsert(node, 5)
#display(newHead)
newHead = SortedInsert(node, 4)
display(newHead)
