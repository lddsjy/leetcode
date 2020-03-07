# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        rec = {}
        for i in numbers:
            if i in rec:
                rec[i] +=1
            else:
                rec[i] = 1
        print(rec)
        for num in rec:
            print(num)
            if rec[num] > len(numbers)/2:
                return num
        return 0

s = Solution()
print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))