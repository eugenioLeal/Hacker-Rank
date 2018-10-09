#!/bin/python3

# Terminated due to timeout :(

import math
import os
import random
import re
import sys

def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    result = 0
    length = len(s)
    subsList = [s[i:j+1] for i in range(length) for j in range(i,length)]
    subsList.sort(key=len)
    n = len(subsList)
    for i in range(n-1):
        for j in range(i+1,n):
            if len(subsList[i]) != len(subsList[j]):
                break
            else:
                if is_anagram(subsList[i],subsList[j]):
                    result += 1
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()