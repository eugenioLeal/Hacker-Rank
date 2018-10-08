#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    for i in queries:
        startRange = i[0]-1
        endRange = i[1]-1
        sumBy = i[2]
        for j in range(n):
            if startRange <= j and endRange >= j:
                arr[j] += sumBy
    return max(arr)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
