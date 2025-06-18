#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    j = 1
    arr = sorted(arr)
    result = 0
    for i in range(len(arr)):
        while j < len(arr):
            #print(arr[j]," ans ", arr[j] - arr[i], arr[i], "i",i, "j", j)
            retemp = arr[j] - arr[i]
            if (retemp == k):
                result +=1
                j += 1
            elif retemp > k:
                break
            elif retemp < k:
                j += 1    
    return result 
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
