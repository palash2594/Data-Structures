# https://www.hackerrank.com/challenges/crush/problem

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    zeroes = [0] * (n + 1)
    for i in range(len(queries)):
        m, n, incr = queries[i][0], queries[i][1], queries[i][2]
        zeroes[m - 1] += incr
        zeroes[n] -= incr

    max = temp = 0
    print(zeroes)
    for i in zeroes:
        temp = temp + i
        if temp > max: max = temp

    return max


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)