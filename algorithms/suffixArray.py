import math
import os
import random
import re
import sys

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
        for i in range(1, tlen):
            nextindex = suffixes[i].index + k//2
            suffixes[i].rank[1] = suffixes[suffixInd[nextindex]].rank[0] if nextindex < tlen else -1                        
        suffixes.sort(key = lambda x:(x.rank[0], x.rank[1]))
        k *= 2
    suffixA = [suffix.index for suffix in suffixes]    
    #print(suffixA)
    return suffixA  
