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

	# print(sortDict)
	# print(sortedArr)
	# print(visited)

	i = 0
	while False in visited :
		visited[i] = True
		if visited[sortDict[arr[i]]] == True :
			cycleCount = 0;
			startingVertex = arr[sortDict[arr[i]]]
			currentVertex = arr[sortDict[arr[i]]]
			while arr[sortDict[currentVertex]] != startingVertex :
				visited[sortDict[currentVertex]] = True
				cycleCount += 1
				currentVertex = arr[sortDict[currentVertex]]
			minSwaps += cycleCount
		else :
			visited[sortDict[arr[i]]] = True
		for j in range(len(visited)) :
			if visited[j] == False :
				i = j
	return minSwaps
	



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    # print(res)

    fptr.write(str(res) + '\n')

    fptr.close()