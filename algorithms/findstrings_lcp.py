#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left
#
# Complete the 'findStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY w
#  2. INTEGER_ARRAY queries
#

def findlcp(s1, s2):
    lcp = 0
    for c1, c2 in zip(s1, s2):
        #print(c1, c2)
        if c1 ==c2:
            lcp+=1
        else:
            break
        #print(lcp)    
    return lcp            

def findStrings(w, queries):
    # Write your code here
    suffix_sort = set()
    for str1 in w:
        for i in range(len(str1)):
            suffix_sort.add(str1[i:len(str1)])
    suffix_list = sorted(suffix_sort)
    #print(suffix_list)        
    rank = []
    for i, s in enumerate(suffix_list):
        if i == 0:
            rank.append(len(s)-1)
        if i > 0 :
            prevS = suffix_list[i-1]
            #print(prevS, s)
            lcp = findlcp(prevS, s)
            rank.append(rank[-1]+len(s[lcp:]))
    #print(rank)
    result = []
    for qq in queries:
        q = qq -1
        rankIndex = bisect_left(rank, q)
        if (rankIndex == len(rank)):
            result.append("INVALID")
            continue
        crank = rank[rankIndex]    
        str2 = suffix_list[rankIndex]
        if q == crank:
            result.append(str2)
        else:
            result.append(str2[:q-crank])    
    return result        
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    w_count = int(input().strip())

    w = []

    for _ in range(w_count):
        w_item = input()
        w.append(w_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = findStrings(w, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
