# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return 'No'
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for j in range(i,len(sequence)):
            if sequence[j] < root:
                return 'No'
        return 'Yes'

s = Solution()
print(s.VerifySquenceOfBST([7,4,6,5]))