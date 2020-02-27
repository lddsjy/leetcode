class Solution {
    long int a = 0;
    long int b = 1;
public:
    int fib(int n) {
        if (n<=1)
            return n;
        else
            for(n;n>1;n--){
               long int temp = a;
                a = b;
                b = temp+b;
            }
        return b%1000000007;
    }
};