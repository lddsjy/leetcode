class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        unordered_map<int,int> m;
        for(auto i:nums){
            m[i]++;
            }
        vector<int> r;
        for(auto i:nums){
            if(m[i]==1) r.push_back(i);
        }
        return r;

    }
};

//空间复杂度O（n）
class Solution {
    public int[] singleNumbers(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums)
            if (!set.add(num))
                set.remove(num);
        
        return set.stream().mapToInt(Integer::intValue).toArray();
    }
}

class Solution {
    public int[] singleNumbers(int[] nums) {
        int xor = 0, len = nums.length;
        for (int num : nums)
            xor ^= num;
        int diff = xor & (-xor);
        int x = 0;
        for (int num : nums) {
            if ((diff & num) != 0)
                x ^= num;
        }
        return new int[]{x, xor ^ x};
    }
}

作者：gfu
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/3chong-fang-fa-by-gfu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution {
    public int[] singleNumbers(int[] nums) {
        int temp = 0;
        for (int num : nums) {
            temp ^= num;
        }
        int mask = temp & (-temp);
        int[] res = new int[2];
        for (int num : nums) {
            if ((num & mask) == 0) {
                res[0] ^= num;
            } else {
                res[1] ^= num;
            } 
        }
        return res;
    }
}

作者：jerry_nju
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/wei-yun-suan-san-bu-zou-by-jerry_nju/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

