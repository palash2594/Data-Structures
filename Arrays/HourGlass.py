# https://www.hackerrank.com/challenges/2d-array/problem

import os

# Complete the array2D function below.
def array2D(arr):
    sum = -999
    for i in range(4):
        for j in range(4):
            val = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            if val > sum:
                sum = val
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)

    fptr.write(str(result) + '\n')

    fptr.close()