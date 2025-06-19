#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringSimilarity(s):
    # Write your code here
    result = 0
    l,r = 0,0
    tlen = len(s) 
    z = [0] * tlen
    
    for x in range(1, len(s)):
        if (x <= r):
            z[x] = min(r-x+1, z[x-l])
        while x+z[x] < tlen and s[x+z[x]] == s[z[x]]:
            z[x] +=1
        if (x + z[x] -1 > r):
            l, r = x, x+z[x] -1
    for x in z:
        result +=x   
    result += tlen
    print(z)                
    return result     
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
