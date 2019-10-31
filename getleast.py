# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        for i in range(k):
            for j in range(len(tinput)-1-i):
                if tinput[j]<tinput[j+1]:
                    tinput[j],tinput[j+1] = tinput[j+1],tinput[j]
        return tinput[-k:]

s = Solution()
print(s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))