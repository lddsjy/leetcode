class Solution {
public:
    vector<double> twoSum(int n) {
        int d[15][70];
        memset(d, 0, sizeof(d));
        for(int i=1; i<=6; i++){
            d[1][i] = 1;
        }
        for(int i = 2; i<=n;i++){
            for(int j = i; j<=6*i; j++){
                for(int k = 1; k<7;k++){
                    if((j-k)<0) break;
                    d[i][j] += d[i-1][j-k];
                }
            }
        }
        vector<double> arr;
        int all = pow(6,n);
        for(int i = n; i<=6*n; i++){
            if(d[n][i]!=0) arr.push_back(d[n][i]*1.0/all);
        }
        return arr;

    }
};