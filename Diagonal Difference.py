#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lr = 0
    rl = 0
    l = len(arr[0])
    counter = l - 1
    for i in range(l):
        lr = lr + arr[i][i]
        rl = rl + arr[i][counter]
        counter = counter - 1
    module = lr - rl    
    if module < 0:
        module = module * -1
    return module        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
