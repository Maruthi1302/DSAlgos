#!/bin/python3
import math
import os
import random
import re
import sys


def swapToSort(arr, idx):
    temp = arr[idx]
    temp2 = arr[temp-1]
    arr[temp-1] = temp
    arr[idx] = temp2
        

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    idx = 0
    swap_count = 0
    while idx < len(arr):
        if idx+1 != arr[idx]:
            swapToSort(arr,idx)
            swap_count = swap_count + 1
        else:
            idx = idx + 1
    return swap_count

def input(x):
    arr = ["7","1 3 5 2 4 6 7"]
    return arr[x]

if __name__ == '__main__':

    n = int(input(0))

    arr = list(map(int, input(1).rstrip().split()))

    res = minimumSwaps(arr)

    print(str(res) + '\n')