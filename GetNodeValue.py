# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def GetNode(head, position):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next

    for i in range(count - position - 1):
        head = head.next

    return head.data

"""
def GetNode(head, position):
    head1 = head
    head2 = head
    count = 0

    while count < position:
        head1 = head1.next
        count += 1

    while head1.next is not None:
        head1 = head1.next
        head2 = head2.next

    return head2.data
"""    
