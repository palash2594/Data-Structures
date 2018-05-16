# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

"""
 Delete Node at a given position in a linked list
 Node is defined as
 """


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Delete(head, position):
    prev = None
    current = head
    count = 0

    while count < position:
        count += 1
        prev = current
        current = current.next

    if count != position:
        print('Not enough nodes in the list')
        return

    if prev is not None:
        prev.next = current.next
    else:
        head = head.next

    return head
