#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'reverseShuffleMerge' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string reverseShuffleMerge(string s) {
   vector<int> arch1(26, 0);
   vector<int> arch2(26, 0);
   for (auto const &ch:s) {
     arch1[ch-'a']++;
   }
   for (int start= 0; start < arch1.size(); start++) {
     arch2[start] = arch1[start]/2;
   }
   int slen = s.length()/2;
   int pos = s.length() - 1;
   int apos = 0;
   string result = "";
   while(apos < slen) {
      bool isReady = false;
      char selected = ' ';
      int indicator = 0;
      int index = 0;
      for (index = pos; index >=0; --index) {
        if ((!isReady || s[index] < selected) && arch2[s[index]-'a']) {
            isReady = true;
            selected = s[index];
            indicator= index;
        }
        arch1[s[index] - 'a']--;
        if (arch1[s[index] - 'a'] < arch2[s[index] - 'a'])
             break;
      }
      for (; index < indicator; ++index) {
        ++arch1[s[index] - 'a'];
      }
      --arch2[selected - 'a'];
      result.push_back(selected);
      apos++;
      pos  = indicator -1;      
   }
   return result; 
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = reverseShuffleMerge(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
