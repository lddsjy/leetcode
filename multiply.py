# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if len(A)<=1:
            return []
        B = [1]*len(A)
        temp = [1]*len(A)
        for i in range(1,len(A)):
            B[i] = B[i-1]*A[i-1]
        for j in range(len(A)-2,-1,-1):
            temp[j] = temp[j+1]*A[j+1]
            B[j] *= temp[j]
        return B

s = Solution()
print(s.multiply([1,2,3]))


