# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n < 1:
            return 0
        num = 0
        while n :
            temp = str(n)
            for i in temp:
                if int(i) == 1:
                    num += 1
            n -= 1
        return num

s = Solution()
print(s.NumberOf1Between1AndN_Solution(13))