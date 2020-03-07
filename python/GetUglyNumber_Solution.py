# -*- coding:utf-8 -*-
# 下一个丑数是序列里某个数×2，*3，*5中的最小
class Solution:
    def GetUglyNumber_Solution(self, index):
        ugly = [1]
        t2 = t3 = t5 = 0
        if index < 1:
            return 0
        while len(ugly) < index:
            while ugly[t2]*2 <= ugly[-1]:
                t2 +=1
            while ugly[t3]*3 <= ugly[-1]:
                t3 +=1
            while ugly[t5]*5 <= ugly[-1]:
                t5 += 1
            ugly.append(min(ugly[t2]*2,ugly[t3]*3,ugly[t5]*5))
        return ugly[-1]

s= Solution()
print(s.GetUglyNumber_Solution(3))
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         ret = [1]
#         if index < 1:
#             return 0
#         if index == 1:
#             return 1
#         tem = []
#         min_ret = 1
#         while index>1:
#             for i in ret:
#                 tem.append(i*2)
#                 tem.append(i*3)
#                 tem.append(i*5)
#             for i in tem:
#                 if i
