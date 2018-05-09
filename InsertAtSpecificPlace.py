

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def display(head):
    while head.next is not None:
        print(head.data, end = ' ')
        head = head.next
    print()

def InsertNth(head, data, position):
    currPos = 0
    prev = None
    current = head

    while currPos < position:
        currPos = currPos + 1
        prev = current
        current = current.next

    newNode = Node(data, current)

    if prev is not None:
        prev.next = newNode
        return head
    else:
        return newNode


head = Node()
head = InsertNth(head, 3, 0)
#display(head)
head = InsertNth(head, 5, 1)
#display(head)
print("Hi")
head = InsertNth(head, 4, 2)
display(head)

head = InsertNth(head, 2, 3)
display(head)
head = InsertNth(head, 10, 1)
display(head)
