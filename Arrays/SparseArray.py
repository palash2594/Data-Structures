# https://www.hackerrank.com/challenges/sparse-arrays/problem

def matchString(string, query):
    if string == query:
        return True
    else: return False


def solve(strings, queries):
    answer =[]
    for query in queries:
        answer.append(strings.count(query))
    """
    for i in queries:
        count = 0
        for j in strings:
            if matchString(i, j):
                count += 1
                print(count)
        answer.append(count)
    """
    return(answer)


if __name__ == '__main__':

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    solve(strings,queries)
    #res = list(map(int,solve(strings, queries)))

    #print(res)



