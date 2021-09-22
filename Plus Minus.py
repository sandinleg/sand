#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    plus = 0
    minus = 0
    zero = 0
    for number in arr:
        if number > 0:
            plus += 1
        elif number < 0:
            minus += 1
        else:
            zero += 1
    print(round(plus / total, 6))
    print(round(minus / total, 6))  
    print(round(zero / total, 6))        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
