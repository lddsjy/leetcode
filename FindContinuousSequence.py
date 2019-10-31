# -*- coding:utf-8 -*-
import math
class Solution:
    def FindContinuousSequence(self, tsum):
        arr = []
        if tsum < 1:
            return []
        for i in range(1,math.ceil(tsum/2)):
            sum = 0
            sub_arr = []
            while sum < tsum:
                sub_arr.append(i)
                sum += i
                i += 1
                if sum == tsum:
                    arr.append(sub_arr)
                    break
        return arr

s = Solution()
print(s.FindContinuousSequence(1))
