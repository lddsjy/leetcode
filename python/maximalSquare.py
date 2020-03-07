class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        r = len(matrix)
        c = len(matrix[0])
        arr = [[0 for i in range(c)] for j in range(r)]
        arr[0] = matrix[0]
        maxl = matrix[0][0]
        for i in range(r):
            arr[i][0] = matrix[i][0]
            maxl = maxl if arr[i][0] < maxl else arr[i][0]
        for i in range(1, r):
            for j in range(1, c):
                arr[i][j] = min(arr[i - 1][j], arr[i - 1][j - 1], arr[i][j - 1]) + 1
                maxl = maxl if arr[i][j] < maxl else arr[i][j]
        return maxl ** 2

s = Solution()
print(s.maximalSquare())