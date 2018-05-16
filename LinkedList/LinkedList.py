

class Node(object):

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError('data not in the list')
        print('data found')
        return current

    def delete(self, data):
        current = self.head
        found = False
        previous = None

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

            if current is None:
                raise ValueError('data not found')
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def display(self):
        current = self.head
        print('List: ', end=' ')

        while current:
            print(current.get_data(), end = ' ')
            current = current.get_next()
        print()





list = LinkedList()

list.insert(2)
list.insert(5)
list.insert(10)
list.insert(3)
list.insert(20)
list.display()
print('Size: ', list.size())
list.search(3)
list.delete(3)
list.display()
