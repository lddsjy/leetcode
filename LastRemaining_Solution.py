# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m <1:
            return -1
        arr = list(range(n))
        i = 0
        while len(arr)>1:
            l = len(arr)
            i = (m-1+i)%l
            arr.pop(i)
        return arr[0]

s  = Solution()
print(s.LastRemaining_Solution(2,2))