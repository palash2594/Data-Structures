

class Node(object):

  def __init__(self, data=None, next_node=None):
      self.data = data
      self.next = next_node

return back the head of the linked list in the below method.

def Insert(head, data):
    newNode = Node(data, head)

    return newNode
