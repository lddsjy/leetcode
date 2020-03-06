class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> r;
        int sum = 0;
        for(int i=1; i< target/2+1; i++){
            sum = i;
            vector<int> arr = {i};
            int j = i+1;
            while(sum<target){                
                sum += j;
                arr.push_back(j);
                if(sum == target){
                    r.push_back(arr);
                    break;
                }
                j++;
            }
        }
        return r;

    }
};