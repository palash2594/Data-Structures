# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def getCount(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def getJoiningPoint(d, headA, headB):

    for i in range(d):
        headA = headA.next

    while headA is not None and headB is not None:
        if headA == headB:
            return headB.data
        print(headA.data, ' ', headB.data)
        headA = headA.next
        headB = headB.next

    return 0

def FindMergeNode(headA, headB):
    c1 = getCount(headA)
    c2 = getCount(headB)

    if c1 > c2:
        d = c1 - c2
        return(getJoiningPoint(d, headA, headB))
    else:
        d = c2 - c1
        return(getJoiningPoint(d, headB, headA))

node = Node(1)
node1 = Node(2, node)
node2 = Node(3, node1)
node3 = Node(4, node2)
node4 = Node(5, node3)
node5 = Node(6, node4)

node6 = Node(7, node2)
node7 = Node(8, node6)
node8 = Node(9, node7)

print(FindMergeNode(node5, node8))

"""
O(N2) implementation
def FindMergeNode(headA, headB):
    while headA is not None:
        headA = headA.next

        current = headB.next
        while current is not None:
            if current == headA:
                return current.data

            current = current.next

    return 0
"""