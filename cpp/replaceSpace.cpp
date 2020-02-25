class Solution {
public:
    string replaceSpace(string s) {
        string newS = "";
        int i = 0;
        int l = s.length();
        for(i=0;i<l;i++){
            if(s[i]==' '){
                newS += "%20";
            }else{
                newS += s[i];
            }
        }
        return newS;

    }
};