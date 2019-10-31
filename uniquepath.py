class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 and n == 0:
            return 0
        import numpy as np
        arr = np.zeros((m, n))
        # arr = [[0 for j in range(n)] for i in range(m)]
        arr[:, 0] = 1
        arr[0, :] = 1
        #arr[0][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        return arr[m - 1][n - 1]




# 思路
# 思路一：排列组合
# 因为机器到底右下角，向下几步，向右几步都是固定的，
# 比如，m=3, n=2，我们只要向下 1 步，向右 2 步就一定能到达终点。
# 所以有 Cm+n−2m−1C_{m+n-2}^{m-1}Cm+n−2m−1​
# Pythondef uniquePaths(self, m: int, n: int) -> int:
#         return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
#
# 作者：powcai
# 链接：https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        print(cur)
        return cur[-1]
# 杨辉三角形，左边+上边
# 作者：powcai
# 链接：https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

s = Solution()
print(s.uniquePaths(3,2))

# class Solution:
# #     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
# #         m, n = len(obstacleGrid[0]), len(obstacleGrid)
# #         dp = [1] + [0]*m
# #         for i in range(0, n):
# #             for j in range(0, m):
# #                 dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
# #         return dp[-2]
# #
# # 作者：yslucas
# # 链接：https://leetcode-cn.com/problems/unique-paths-ii/solution/python3liu-xing-jian-ji-dai-ma-shi-jian-kong-jian-/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#有障碍的路径