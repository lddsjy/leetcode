# -*- coding:utf-8 -*-
# from functools import reduce
# #python3 中 reduce移除了，python2 可以直接用
# class Solution:
#     def Sum_Solution(self, n):
#         return reduce(lambda x,y:x+y,range(1,n+1))
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        return sum(range(1,n+1))
s =Solution()
print(s.Sum_Solution(1))