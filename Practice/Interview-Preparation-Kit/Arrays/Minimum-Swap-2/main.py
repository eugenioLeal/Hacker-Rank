#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	minSwaps = 0
	sortDict = {}
	visited = [False] * len(arr)
	sortedArr = sorted(arr)

	for i, item in enumerate(sortedArr) :
		sortDict[item] = i

	for i in range(len(arr)-1) :

		while arr[i] != i+1 :
			swapKey = arr[i]-1
			temp = arr[i]
			arr[i] = arr[swapKey]
			arr[swapKey] = temp
			minSwaps += 1

	return minSwaps
	



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()