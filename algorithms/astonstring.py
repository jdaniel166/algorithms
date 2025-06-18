#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'ashtonString' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def ashtonString(text, k):
    # Write your code here
    stackp = [("", [i for i in range(len(text))])]    
    while stackp != []:
        prefixstr, startindexes = stackp.pop()
        if k <= len(prefixstr):
            return prefixstr[k-1]
        k -= len(prefixstr)   
        sortedstr = sorted([(text[i], i+1) for i in startindexes if i < len(text)], reverse=True)
        i = 0
        while (i < len(sortedstr)):
            j = i +1
            pre = sortedstr[i][0]
            indexval = [sortedstr[i][1]]
            while j < len(sortedstr) and pre == sortedstr[j][0]:
                indexval.append(sortedstr[j][1])
                j += 1
            stackp.append((prefixstr+pre, indexval))
            i = j      
    return None
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        res = ashtonString(s, k)

        fptr.write(str(res) + '\n')

    fptr.close()
