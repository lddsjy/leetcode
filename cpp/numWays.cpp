class Solution {
public:
    int numWays(int n) {
        int a = 0, b=1;
        int temp = 0, i =0;
       while(i<n){
           i++;
           temp = a;
           a = b;
           b = temp + b;
           b = b%1000000007;
               
       }
        return b;

    }
};