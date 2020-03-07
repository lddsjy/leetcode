# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        dic = {}
        pos = -1
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for item in dic:
            if dic[item] == 1:
                pos = s.index(item)
                break
        return pos

s = Solution()
print(s.FirstNotRepeatingChar('g'))