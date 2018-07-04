# https://www.hackerrank.com/challenges/array-and-simple-queries/problem

def query1(start, end):
    diff = end - start + 1
    for _ in range(diff):
        item = array.pop(end - 1)
        array.insert(0, item)

def query2(start, end):
    diff = end - start + 1
    for _ in range(diff):
        item = array.pop(start - 1)
        array.append(item)

n, m = map(int, input().split())

array = list(map(int, input().split()))

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

for i in range(m):
    if queries[i][0] == 1:
        query1(queries[i][1], queries[i][2])
    else:
        query2(queries[i][1], queries[i][2])

print(abs(array[0] - array[n - 1]))
print(*array)