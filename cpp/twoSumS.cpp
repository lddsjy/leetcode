class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> arr;
        int i = 0, j = nums.size()-1;
        while(i<j){
            int sum = nums[i] + nums[j];
            if(sum<target) i++;
            else if(target == sum){
                arr.push_back(nums[i]);
                arr.push_back(nums[j]);
                return arr;
            }
            else j--;
        }
        return arr;
        

    }
};
//一头一尾开始向中间找，小了增加i，大了减少j