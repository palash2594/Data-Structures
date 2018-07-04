# https://www.hackerrank.com/challenges/array-and-simple-queries/problem

def query1(start, end):
    diff = end - start + 1
    newArray = array1[(start - 1) * 2 : (end - 1) * 2 + 2] + array1[ : (start - 1) * 2] + array1[(end - 1) * 2 + 2:]
    return newArray

def query2(start, end):
    diff = end - start + 1
    newArray = array1[ : (start - 1) * 2] + array1[(end - 1) * 2 + 2:] + array1[(start - 1) * 2 : (end - 1) * 2 + 2]
    return newArray

n, m = map(int, input().split())

array1 = input() + ' '

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

for i in range(m):
    if queries[i][0] == 1:
        array1 = query1(queries[i][1], queries[i][2])
    else:
        array1 = query2(queries[i][1], queries[i][2])

print(abs(int(array1[0]) - int(array1[len(array1) - 2])))
for i in range(n):
    print(array1[i*2], end = ' ')