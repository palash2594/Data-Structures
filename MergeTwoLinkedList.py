
class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def MergeLists(headA, headB):

    if headA is None:
        return headB
    if headB is None:
        return headA

    pointer = None

    if headA.data < headB.data and pointer is None:
        pointer = headA
        headA = headA.next
    elif headA.data > headB.data and pointer is None:
        pointer = headB
        headB = headB.next

    finalHead = pointer
    while headA is not None and headB is not None:

        if headA.data < headB.data:
            pointer.next = headA
            pointer = pointer.next
            headA = headA.next

        elif headA.data > headB.data:
            pointer.next = headB
            pointer = pointer.next
            headB = headB.next

    while headA is not None:
        pointer.next = headA
        headA = headA.next

    while headB is not None:
        pointer.next = headB
        headB = headB.next

    return finalHead
