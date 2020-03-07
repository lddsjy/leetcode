# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return None
        fun = lambda n1,n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        sorted(numbers,cmp=fun)
        return ''.join([str(i) for i in numbers])
