# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, n):
        if n == 1:
            return 1
        if n < 1:
            return None
        id = 1
        a = 1
        b = 1
        while id < n:
            id +=1
            c = a+b
            a = b
            b = c
        return c

s = Solution()
print(s.jumpFloor(4))
# class Solution:
#     def Fibonacci(self, n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n < 0:
#             return None
#         id = 1
#         a = 0
#         b = 1
#         while id < n:
#             id +=1
#             c = a+b
#             a = b
#             b = c
#         return c
#
# s = Solution()
# print(s.Fibonacci(-1))
#

