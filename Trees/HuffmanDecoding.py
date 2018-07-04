# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None

def decodeHuff(root , s):
    answer = ''
    current = root
    for i in s:
        if i == '1':
            current = current.right
        else:
            current = current.left
        if current.left == None and current.right == None:
                answer = answer + current.data
                current = root

    return answer