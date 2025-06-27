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
