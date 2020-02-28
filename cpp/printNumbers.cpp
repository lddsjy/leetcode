class Solution {
public:
    vector<int> printNumbers(int n) {
        vector<int> ret;
        for(int i = 1; i < pow(10,n); i++){
            ret.push_back(i);
        }
        return ret;

    }
};