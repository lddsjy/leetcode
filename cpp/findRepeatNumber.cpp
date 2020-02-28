// 方法一：使用集合
// 我们遍历一遍数组，判断 nums[i] 是否存在于集合中，如果存在，则返回该值；如果不存在，将该值添加到集合中。
// 复杂度分析

// 时间复杂度：O(N)O(N)O(N)。最坏条件下，我们遍历了整个数组。
// 空间复杂度：O(N)O(N)O(N)。使用了哈希表。

// 在这里，将集合换成哈希表实现也可以。其中，哈希表的格式为 {值：索引}。

// 方法二：排序
// 思路很简单，将数组排序，相同的数会挨在一起，因此如果碰到两个相邻的数相等，立即返回即可。但是排序会花费 O(NlogN) 的时间复杂度。

// 方法三：原地实现
// 注意题目中提到 “长度为 nnn 的数组 numsnumsnums 里的所有数字都在 0～n−10～n-10～n−1 的范围内”。因此我们通过交换 nums[i] 和 nums[nums[i]] 使得数组元素等于索引，这样如果再次找到一个相同数字，但索引不同，则表明找到了重复数字。
 // 代码
// pythonclass Solution:
    // def findRepeatNumber(self, nums: List[int]) -> int:
        // for idx, val in enumerate(nums):
            // if idx != val and nums[val] == val: return val # 找到重复数字
            // nums[val], nums[idx] = nums[idx], nums[val]

 // 复杂度分析

// 时间复杂度：O(N)O(N)O(N)，对数组进行一趟遍历。
// 空间复杂度：O(1)O(1)O(1)，没有使用额外空间，对数组进行原地修改。

// 作者：z1m
// 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/jian-ji-ha-xi-biao-by-ml-zimingmeng/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        std::map<int,int> mymap;
        int l = nums.size();
        for(int i=0;i<l;i++){
            if (mymap.count(nums[i])>0) return nums[i];
            else mymap.insert ( std::pair<int,int>(nums[i],1) );
        }
        
        return NULL;
    }
};
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        set<int> count;
        for(auto i:nums){
            if(count.count(i) == 1){
                return i;
            }else{
                count.insert(i);
            }
        }
        return 0;
    }
};


//数字范围在0到n-1
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        bool flag[nums.size()];
        //初始化为false 
        memset(flag, false, sizeof(flag));
        for(int i = 0; i < nums.size(); i++)
            if(flag[nums[i]])
                return nums[i];
            else
                flag[nums[i]] = true;
        return -1;
    }
};
