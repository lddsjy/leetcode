class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        tmp1 = nums[1]
        tmp0 = 0
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            #从二开始选到最后一个，从一开始选到倒数第二个，比较这两者，大的那个为结果
            tmp2 = max(tmp0+nums[i],tmp1)
            tmp0,tmp1 = tmp1,tmp2
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        print(nums,tmp2)
        return max(nums[-2],tmp2)

s = Solution()
print(s.rob([2,3,2]))