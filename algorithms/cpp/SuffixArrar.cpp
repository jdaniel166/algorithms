#include <bits/stdc++.h>
using namespace std;

struct SuffixNode {
   int index = 0;
   std::pair<int, int> rank;
   int operator<(const SuffixNode & other2) {
       return (rank.first == other2.rank.first) ? 
          (rank.second < other2.rank.second ? 1 : 0)
          :(rank.first < other2.rank.first ? 1 : 0); 
   } 
}; 

std::vector<int> findLcp(const std::vector<int> &suffixA, std::string s) {
    int slen = suffixA.size();
    std::vector<int> lcpArray(slen, 0);
    std::vector<int> invSuffix(slen, 0);
    for (int start = 0; start < slen; start++) {
        invSuffix[suffixA[start]] = start;
    } 
    auto k = 0;
   for (int start = 0; start < slen; start++) {
        if (invSuffix[start] == slen -1) {
            k = 0;
            continue;
        }
        auto j = suffixA[invSuffix[start]+1];
        while (start + k < slen && j+k < slen && s[start+k] == s[j+k]) {
            k++;
        } 
        lcpArray[invSuffix[start]] = k ;
        if (k > 0) k--;  
   } 
   return lcpArray;
}
 
std::vector<int> computeSuffixA(std::string s) {
    std::vector<int> result;
    int slen = s.size();
    auto startIndex = 'a';
    std::vector<SuffixNode> suffixes;
    auto index = 0;
    auto k = 4;
    for (;index < slen-1;index++) {
        suffixes.push_back(SuffixNode{index,{s[index] - startIndex, s[index+1] - startIndex}});
    }

    suffixes.push_back(SuffixNode{index,{s[index] - startIndex, -1}});   
    sort(suffixes.begin(), suffixes.end());
    std::vector<int> suffixesInd(slen, 0);
    while (k <= 2*slen) {
        auto prev_rank = suffixes[0].rank.first, rank = 0;
        suffixes[0].rank.first = rank;
        suffixesInd[suffixes[0].index] = 0;
        for (auto start = 1;start < slen; start++) {
            if (suffixes[start].rank.first == prev_rank &&
              suffixes[start].rank.second == suffixes[start-1].rank.second ) {
                prev_rank = suffixes[start].rank.first;
                suffixes[start].rank.first = rank;
              } else {
                prev_rank = suffixes[start].rank.first;
                rank++;
                suffixes[start].rank.first = rank;
              }
              suffixesInd[suffixes[start].index] = start;
        }
        for (auto start = 0;start < slen; start++) {
            auto next = suffixes[start].index + k/2;
            suffixes[start].rank.second = -1;
            if (next < slen) {
               suffixes[start].rank.second = suffixes[suffixesInd[next]].rank.first;
            } 
        }
        sort(suffixes.begin(), suffixes.end());
        k *= 2;
    }    
     for (auto const & dt: suffixes) {
        result.push_back(dt.index);
        std::cout << dt.index <<" ";
     }
    return result;
}
