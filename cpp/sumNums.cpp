class Solution {
public:
    int sumNums(int n) {
        int ans = n;
        ans and (ans += sumNums(n-1));
        return ans; 

    }
};