
class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def ReversePrint(head):

    list = []
    while head is not None:
        list.append(head.data)
        head = head.next

    for i in range(len(list) - 1, -1, -1):
        print(list[i])