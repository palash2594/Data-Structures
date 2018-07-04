# https://www.hackerrank.com/challenges/median/problem

class Node(object):
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None

class AVL_Tree(object):
    def insertNode(self, key, root):
        if root is None:
            return Node(key)

        elif root.data > key:
            root.left = self.insertNode(key, root.left)
        else:
            root.right = self.insertNode(key, root.right)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Left-Left case
        if balance > 1 and root.left.data > key:
            return self.rotateRight(root)

        # Right-Right case
        if balance < -1 and root.right.data < key:
            return self.rotateLeft(root)

        # Left-Right case
        if balance > 1 and root.left.data < key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Right-Left case
        if balance < -1 and root.right.data > key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if root is None:
            return -1
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

def removeData(root, key):
    prev = None
    while root is not None:
        if root.data == key:
            if prev is None:



def median(a, x):
    myTree = AVL_Tree()
    root = None
    leftCount = 0
    rightCount = 0

    for i in range(len(a)):
        if a[i] == 'a':
            if root != None:
                if x[i] > root.data: rightCount += 1
                else: leftCount += 1
            root = myTree.insertNode(x[i])
            if leftCount == rightCount:
                print(root.data)
            elif leftCount > rightCount:
                print((root.data + root.left.data) / 2)
            else:
                print((root.data + root.right.data) / 2)
        else:
            if root == None:
                print('Wrong!')
            else:
                pass


if __name__ == '__main__':
    N = int(input())
    s = []
    x = []
    for i in range(0, N):
        tmp = input().strip().split(' ')
        a, b = [xx for xx in tmp]
        s.append(a)
        x.append(int(b))
    median(s, x)