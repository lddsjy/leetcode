class Solution {
public:
    vector<int> exchange(vector<int>& nums) {
        int i = 0, l = nums.size();
        int j = 0;
        while(i<l){
            if(nums[i]%2==0){
                nums.push_back(nums[i]);
                nums.erase(nums.begin()+i);
            }
            else i++;
            j ++ ;
            if(j == l) break;
        }
        return nums;

    }
};

    vector<int> exchange(vector<int>& nums) {
        if (nums.empty()) return nums;
        size_t l = 0, r = nums.size() - 1;
        
        while (l < r) {
            while (l < r && nums[l] % 2 == 1) ++l;
            while (l < r && nums[r] % 2 == 0) --r;
            
            if (l < r) swap(nums[l], nums[r]);
        }
        
        return nums;
    }