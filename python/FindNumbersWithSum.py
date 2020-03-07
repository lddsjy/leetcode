# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        arr = []
        product = []
        for i in array:
            if 2*i >= tsum:
                break
            if tsum-i in array[array.index(i):]:
                arr.extend([i,tsum-i])
                break
        #         arr.append([i,tsum-i])
        #         product.append([i*(tsum-i)])
        # if product:
        #     index = product.index(min(product))
        #     arr = arr[index]

        return arr

s = Solution()
print(s.FindNumbersWithSum([1,2,3,4,5],6))
