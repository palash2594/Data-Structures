# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    slowPointer = head
    fastPointer = head

    while slowPointer != None and fastPointer.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next

        if slowPointer == fastPointer:
            return 1 # cycle present

    return 0 # no cycle present