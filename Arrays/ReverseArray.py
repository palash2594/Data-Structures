
import os
import sys

#
# Complete the reverseArray function below.
#
def reverseArray(a):
    res = list()
    flag = 0
    for i in range(len(a), 0, -1):
#       print(a[i - 1], end = ' ')
        res.append(a[i - 1])
        flag += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()