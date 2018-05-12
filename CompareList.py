#https://www.hackerrank.com/challenges/compare-two-linked-lists/problem


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def CompareLists(headA, headB):
    while headA is not None and headB is not None:
        if headA.data == headB.data:
            headA = headA.next
            headB = headB.next
            continue
        else:
            return 0

    if headA is not None or headB is not None:
        return 0
    else:
        return 1
