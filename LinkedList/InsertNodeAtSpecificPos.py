
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

    newNode = Node(data)

    if position == 0:
        newNode.next = head
        return newNode

    previous = head
    current = head.next

    for i in range(position - 1):
        print('i=',i)
        if position == 1:
            previous.next = newNode
            newNode.next = current
            return head
        previous = previous.next
        current = current.next

    newNode.next = current
    previous.next = newNode

    return head

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
