class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        int maxN = nums[0];
        for(int i = 1; i < nums.size(); i++){
            nums[i] = max(nums[i], nums[i-1]+nums[i]);
            // way one
            //if(maxN < nums[i]) maxN = nums[i];            
        }
        //way two
        return nums[max_element(nums.begin(),nums.end())-nums.begin()];

    }
};