# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        num = []
        if len(numbers) != 5:
            return False
        for i in numbers:
            num.append(i) if i else None
        #无重复数字
        if len(num) != len(set(num)):
            return False
        if max(num) - min(num) >= 5:
            return False
        return True
# import collections
# class Solution:
#     def IsContinuous(self, numbers):
#         if len(numbers) != 5:
#             return False
#         c = collections.Counter(numbers)
#         # print(c,dict(c))
#         # c = sorted(c.values())
#         if c.most_common(1)[0][1] > 1 and c.most_common(1)[0][0] != 0:
#             return False
#         num = set(numbers)
#         if min(num) == 0:
#             num.remove(0)
#         if max(num)-min(num) >= 5:
#             return False
#         return True

s = Solution()
print(s.IsContinuous([0,2,2,1,0]))