#!/bin/python3

import math
import os
import random
import re
import sys
import resource

#
# Complete the 'maxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING t as parameter.
#

def lcpA(s, suffixA):
    n = len(suffixA)
    lcp = [0] * n
    invsuffix = [0] * n
    for i in range(n):
        invsuffix[suffixA[i]] = i    
    k = 0
    for i in range(n):
        if invsuffix[i] == n-1:
            k = 0
            continue
        j = suffixA[invsuffix[i]+1]
        while (i + k < n and j + k < n and s[i+k] == s[j+k]):
            k +=1 
        lcp[invsuffix[i]] = k
        if (k > 0):
            k -=1        
    return lcp

def findArea(lcps, stackp, i):
    slast = stackp.pop()
    temp = 0
    area = 0
    if stackp == []:
        temp = i + 1
    else:
        temp = i - stackp[-1]    
    area =  lcps[slast] * temp
    return area
    
class SuffixNode:    
    def __init__(self, index, rank1, rank2):
        self.index = index
        self.rank = [rank1, rank2]
           
def buildSuffixArray(s):
    # Write your code here
    tlen = len(s)
    startIndex = ord("a")
    suffixes  = [SuffixNode(i, ord(s[i])-startIndex, ord(s[i+1])-startIndex if i+1 < tlen else -1) for i in range(tlen)]
    suffixes.sort(key = lambda x : (x.rank[0], x.rank[1])) # suffix array is sorted 
    suffixInd = [0] * tlen 
    k = 4
    while k <= 2*tlen:
        rank, prev_rank = 0, suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        suffixInd[suffixes[0].index] = 0
        for i in range(1,tlen):
            if (suffixes[i].rank[0] == prev_rank and
                suffixes[i].rank[1] == suffixes[i-1].rank[1]):
                prev_rank = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank
            else:
                prev_rank = suffixes[i].rank[0]
                rank +=1
                suffixes[i].rank[0] = rank
            suffixInd[suffixes[i].index] = i            
        for i in range(tlen):
            nextindex = suffixes[i].index + k//2
            suffixes[i].rank[1] = suffixes[suffixInd[nextindex]].rank[0] if nextindex < tlen else -1                        
        suffixes.sort(key = lambda x:(x.rank[0], x.rank[1]))
        k *= 2
    suffixA = [suffix.index for suffix in suffixes]    
    #print(suffixA)
    return suffixA       
            
def maxValue(t):
    tlen = len(t)
    maxval = 0
    suffix_sorted = buildSuffixArray(t)
    lcps = lcpA(t, suffix_sorted)
    #print(suffix_sorted)    
    #print(lcps)     
    stackp = []
    i = 0

    while(i < len(lcps)):
        if (stackp == [] or lcps[stackp[-1]] <= lcps[i]):
            stackp.append(i)
            i +=1
        else:
            temp = findArea(lcps, stackp, i)
            if (maxval < temp):
                maxval = temp
    while (stackp != []):
        temp = findArea(lcps, stackp, i)   
        if (maxval < temp):
            maxval = temp    
    if (maxval < tlen):
        maxval = tlen        
    return maxval
   
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)

    fptr.write(str(result) + '\n')

    fptr.close()
