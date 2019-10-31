# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    def Insert(self, num):
        self.arr.append(num)
        self.arr = sorted(self.arr)
    def GetMedian(self,arr):
        if len(self.arr)==0:
            return None
        if len(self.arr)%2==0:
            mid = len(self.arr)//2
            return (self.arr[mid-1]+self.arr[mid])/2
        else:
            mid = len(self.arr) // 2
            return self.arr[mid]

s = Solution()
for i in [5,2,3,4,1,6,7,0,8]:
    s.Insert(i)
    print(s.GetMedian(s.arr))
