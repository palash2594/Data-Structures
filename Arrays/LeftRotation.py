# https://www.hackerrank.com/challenges/array-left-rotation/problem

# Complexity O(n)
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    count = 0
    curPos = 0
    current = a[curPos]
    while count != len(a):
        if curPos < d: # for elements whose position is less then 'd'
            curPos = len(a) + curPos - d # finding new position where the current element needs to be put
            temp = current # copying the current item to temp
            current = a[curPos] # assigning new current value to current
            a[curPos] = temp # puting down the old current value to new position
        else:
            curPos -= d
            temp = current
            if len(a) / 2 == d: # checking is done so as to move current pointer
                current = a[curPos + 1]
                a[curPos] = temp
                curPos += 1
            else:
                current = a[curPos]
                a[curPos] = temp

        count += 1
    for i in range(len(a)):
        print(a[i], end = ' ')
    """
    temp = a[0]
    for curPosin range(d, len(a), 1):
        a[i] = a[curPos+ d]
    """