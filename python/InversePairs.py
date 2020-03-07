# -*- coding:utf-8 -*-
count = 0
class Solution:
    def InversePairs(self, data):
        global count
        self.merge(data)
        return count%1000000007
    def merge(self,lists):
        global count
        if len(lists) <= 1:
            return lists
        num = int(len(lists)/2)
        left = self.merge(lists[:num])
        right = self.merge(lists[num:])
        r, l=0, 0
        result = []
        while l<len(left) and r<len(right):
            #print('*',left[l],l,left)
            if left[l] < right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r +=1
                count += len(left)-l
        result.extend(left[l:])
        result.extend(right[r:])
        return result
# count = 0
# class Solution:
#     def InversePairs(self, data):
#         global count
#         def MergeSort(lists):
#             global count
#             if len(lists) <= 1:
#                 return lists
#             num = int( len(lists)/2 )
#             left = MergeSort(lists[:num])
#             right = MergeSort(lists[num:])
#             r, l=0, 0
#             result=[]
#             while l<len(left) and r<len(right):
#                 if left[l] < right[r]:
#                     result.append(left[l])
#                     l += 1
#                 else:
#                     result.append(right[r])
#                     r += 1
#                     count += len(left)-l
#             result += right[r:]
#             result += left[l:]
#             return result
#         MergeSort(data)
#         return count%1000000007
s = Solution()
print(s.InversePairs([1,2,3,4,5,6,7,0]))

