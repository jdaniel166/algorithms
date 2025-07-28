#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'virusIndices' function below.
 *
 * The function accepts following parameters:
 *  1. STRING p
 *  2. STRING v
 */

struct SuffixNode {
   int index = 0;
   std::pair<int, int> rank;
   int operator<(const SuffixNode & other2) {
       return (rank.first == other2.rank.first) ? 
          (rank.second < other2.rank.second ? 1 : 0)
          :(rank.first < other2.rank.first ? 1 : 0); 
   } 
}; 

auto findLcp(const std::vector<int> &suffixA, std::string s, string v) {
    std::vector<int>lcpa(s.length()+1, 0);
    for (int i = 0, j = s.length(), k = 0; i <= j && k <= v.length(); k++) {
        //std::cout<<i<<" " << j << " " << k <<endl;
        while (i <= j && s[suffixA[i] + k] < v[k]) lcpa[suffixA[i++]] = k;
        while (i <= j && s[suffixA[j] + k] > v[k]) lcpa[suffixA[j--]] = k;
    }
        //for (int i = 0;i < s.length(); i++) {
        //       std::cout<<"P="<<lcpa[i] <<" ";   
       // }
       // std::cout<<endl;
   return lcpa;   
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
     result.push_back(s.length()); 
     for (auto const & dt: suffixes) {
        result.push_back(dt.index);
        //std::cout << dt.index <<" ";
     }
    result.push_back(0); 
    return result;
}

void virusIndices(string p, string v) {
    // Print the answer for this test case in a single line
    int ll = p.length();
    auto vll = int(v.length());
    if (ll < vll) std::cout<< "No Match!" << endl;
    auto suffixA = computeSuffixA(p);
    std::vector<int> result;
    auto prefixLcp = findLcp(suffixA, p, v);
    std::reverse(p.begin(), p.end());
    std::reverse(v.begin(), v.end());
    auto suffixB = computeSuffixA(p);
    auto suffixLcp = findLcp(suffixB, p, v);
    reverse(suffixLcp.begin(), suffixLcp.begin()+p.length());
    for (int i = 0, j = v.length()-1;j<p.length();i++, j++) {
        //std::cout<<prefixLcp[i] << " "<<suffixLcp[j] <<endl;
        if (prefixLcp[i]+suffixLcp[j] >= v.length()-1) {
             result.push_back(i);
        }
    }
    if (result.empty()) std::cout<< "No Match!" << endl;
    else {
        for (auto const &d:result) {
           std::cout<<d<<" ";            
        }
        std::cout<<endl;
    }
}

int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        string p = first_multiple_input[0];

        string v = first_multiple_input[1];

        virusIndices(p, v);
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
