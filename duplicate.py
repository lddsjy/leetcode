# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        dic = {}
        for i in numbers:
            if i in dic:
                duplication[0] = i
                print(duplication[0])
                return True
            else:
                dic[i] = 1
        return False

s = Solution()
print(s.duplicate([2,1,3,1,4],[0]))

# -*- coding:utf-8 -*-
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        flag=False
        c=collections.Counter(numbers)
        for k,v in c.items():
            if v>1:
                duplication[0]=k
                flag=True
                break
        return flag