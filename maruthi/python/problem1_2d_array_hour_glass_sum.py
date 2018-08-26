#problem statement
#https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#2D Array - DS
# Hour glass sum.
#!/bin/python3
import math
import os
import random
import re
import sys
import itertools

def input(x):
    arr =["-1 -1 -1 0 0 0",
            "0 -1 0 0 0 0"
            ,"-1 -1 -1 0 0 0"
            ,"0 -9 -2 -4 -4 0"
            ,"0 0 0 -2 0 0"
            ,"0 0 -1 -2 -4 -10"]
    return arr[x]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    indexTillToIterate = 2
    arrayWidth = len(arr[0])
    arrayHeight = len(arr)
    greatestSum = 0
    firstTime = True
    for jdx,idx in itertools.product(range(arrayWidth - indexTillToIterate),range(arrayHeight-indexTillToIterate)):
        sum = arr[jdx][idx] + arr[jdx][idx+1] + arr[jdx][idx+2]+arr[jdx+1][idx+1]+arr[jdx+2][idx]+arr[jdx+2][idx+1]+arr[jdx+2][idx+2]
        if firstTime:
            greatestSum = sum
            firstTime = False
        elif greatestSum < sum:
            greatestSum = sum
    return greatestSum
                
if __name__ == '__main__':

    arr = []
   
    for x in range(6):
        arr.append(list(map(int, input(x).rstrip().split())))

    result = hourglassSum(arr)
    print(str(result) + '\n')
    

