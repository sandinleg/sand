#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ampm = s[8:10]
    if ampm == "PM":
        hours = int(s[0:2])
        if hours == 12:
            hours = hours
        else:
            hours += 12
        s = str(hours) + s[2:8]
        return s
    if ampm == "AM":
        hours = int(s[0:2])
        if hours == 12:
            hours -= 12
        else:
            hours = hours
        hours = "0" + str(hours)
        s = hours + s[2:8]
        return s 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
