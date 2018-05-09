
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    current  = head
    while current.next is not None:
        current = current.next

    current.next = newNode

    return head

head = Node(1)
print(Insert(head, 3).data)
Insert(head, 247)
Insert(head,678)
Insert(head, 159)
print(Insert(head, 17).data)
