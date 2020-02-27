class Solution {
public:
    char firstUniqChar(string s) {
        vector<int> help(26,0);
        for(char c:s)
            help[c-'a']++;
        for(char c:s)
            if(help[c-'a']==1) return c;
        return ' ';

class Solution {
public:
    char firstUniqChar(string s) {
        vector<int> d(128,0);
        int i=0,j=0;
        for(int i=0;i<s.length();i++){
            d[s[i]]++;
            while(d[s[j]]>1)j++;
        }
        if(j<s.length())return s[j];
        return ' ';
    }
};