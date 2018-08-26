#!/bin/python3

import math
import os
import random
import re
import sys

# rotate array helper
def rotateOneTimeLeft(a):
    firstElem = a[0]
    for x in range(len(a)-1):
        a[x] = a[x+1]
    a[len(a)-1] = firstElem
    return a

def rotateOneTimeRight(a):
    length = len(a)
    lastElem = a[length-1]
    for x in range(length-1):
        a[length-1-x] = a[length-2-x]
    a[0] = lastElem
    return a
# Complete the rotLeft function below.
def rotLeftOld(a, d):
    lengthtoRotate = d%len(a)
    if lengthtoRotate < (len(a)-lengthtoRotate):
        for _ in range(lengthtoRotate):
            a = rotateOneTimeLeft(a)
    else:
        for _ in range(len(a)-lengthtoRotate):
            a = rotateOneTimeRight(a)
    return a

def rotLeft(a,d):
    arrayLen = len(a)
    result = [0]*arrayLen
    for x in range(arrayLen):
        result[(2*arrayLen-(d-x))%arrayLen] = a[x]
    return result
        
# Need to work on this currently its wrong.
def rotLeftInPlace(a,d):
    arrayLen = len(a)
    idx = 0
    temp = a[idx]
    for _ in range(arrayLen):
        pairIdx = (2*arrayLen-(d-idx))%arrayLen
        temp2 = a[pairIdx]
        a[pairIdx] = temp
        temp = temp2
        idx = pairIdx
    return a

def input(x):
    arr = ["5 4","1 2 3 4 5"]
    return arr[x]

if __name__ == '__main__':

    nd = input(0).split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input(1).rstrip().split()))

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))
    print('\n')
