#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag = {}
    for i in magazine:
        mag[i] = 0
    for i in magazine:
        mag[i] += 1
    for i in note:
        if i not in mag:
            print("No")
            return
        mag[i] -= 1
        if mag[i] < 0:
            print("No")
            return
    print("Yes")
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)