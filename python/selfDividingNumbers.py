class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        arr = []
        for i in range(left, right + 1):
            flag = sum([i % (int(j)) for j in str(i) if int(j)])
            if not flag:
                arr.append(i)
        return arr


s = Solution()
print(s.selfDividingNumbers(1,22))