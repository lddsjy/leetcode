# -*- coding:utf-8 -*-
import random
class Solution:
    def reOrderArray(self, array):
        if array == None:
            return []
        odd = []
        even = []
        for i in array:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        array = odd+even
        return array

s = Solution()
a = random
print(s.reOrderArray([]))
