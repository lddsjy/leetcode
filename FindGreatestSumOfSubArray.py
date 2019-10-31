# -*- coding:utf-8 -*-
#动态规划
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return None
        dp = [array[0]]
        for i in range(1,len(array)):
            print(dp)
            dp.append(max(array[i],dp[i-1]+array[i]))

        return max(dp)

s = Solution()
print(s.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))