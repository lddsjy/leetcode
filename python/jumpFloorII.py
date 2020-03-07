# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number < 1:
            return None
        way = 1
        number -= 1
        # while number:
        #     way *= 2
        #     number -= 1
        way = pow(2,number)
        return way

s = Solution()
print(s.jumpFloorII(2))