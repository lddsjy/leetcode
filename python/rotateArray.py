# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        return min(rotateArray)
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         # write code here
#         left = 0
#         right = len(rotateArray)-1
#         mid = (left+right)>>1
#         if not rotateArray:
#             return 0
#         while left <= right:
#             print(mid)
#             if rotateArray[mid] <= rotateArray[left] and rotateArray[mid] <= rotateArray[right]:
#                 return rotateArray[mid]
#             if rotateArray[mid] >= rotateArray[right]:
#                 left = mid+1
#                 mid = (left + right) >> 1
#             else:
#                 right = mid-1
#                 mid = (left + right) >> 1
#
#         return rotateArray[mid]

s = Solution()
print(s.minNumberInRotateArray([3,4,5,1,2]))