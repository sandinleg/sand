#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    i = 1
    while i <= n:
        line = ' ' * (n - i) + '#' * i
        print(line)
        i += 1
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
