# https://www.hackerrank.com/challenges/dynamic-array/problem

#
def getSeq(x, lastAnswer, n):
    return (x ^ lastAnswer) % n

def dynamicArray(n, queries):
    seqList = [list() for i in range(n)]

    lastAnswer = 0

    for line in queries:
        seq = getSeq(line[1], lastAnswer, n)
        if line[0] == 1:
            seqList[seq].append(line[2])

        if line[0] == 2:
            lastAnswer = seqList[seq][line[2] % len(seqList[seq])]
            print(lastAnswer)

"""
    for i in range(queries):
        query = list(map(int, input().split()))
        print(query)
        if query[0] == 1:
            print('hello')
            seq = (query[1] ^ lastAnswer) % n
            seqList[seq].append(query[2])

        if query[0] == 2:
            seq = (query[1] ^ lastAnswer) % n
            lastAnswer = seqList[seq][query[2]]
            print(lastAnswer)


dynamicArray(2, 5)
"""
nq = input().split()
n = int(nq[0])
q = int(nq[1])

queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

dynamicArray(n, queries)