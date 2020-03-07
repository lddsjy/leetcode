# -*- coding:utf-8 -*-
class Solution():
    def maxInWindows(self, num, size):
        arr = []
        if len(num)>=size and size>0:
            for i in range(len(num)-size+1):
                temp = num[i:i+size]
                arr.append(max(temp))
        return arr

s = Solution()
print(s.maxInWindows([2],1))