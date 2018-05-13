
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def RemoveDuplicates(head):

    if head == None or head.next == None:   
        return head

    current = head

    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head