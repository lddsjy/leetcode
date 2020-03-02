class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> dp = {0};
        if(prices.size()>1){
            int minp = prices[0];
            for(int i=1; i<prices.size();i++){
                
                dp.push_back(max(prices[i]-minp,dp[i-1]));
                minp = min(minp,prices[i]);
            }
            
        }
        return dp[dp.size()-1];

    }
};