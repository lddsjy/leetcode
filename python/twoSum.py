class Solution:
    def twoSum(self, n: int) -> List[float]:
        d = [[0 for i in range(6*n)] for j in range(n)]
        for i in range(6):
            d[0][i] = 1
        for i in range(1,n):
            for j in range(6*n):
                for k in range(6):
                    d[i][j] += d[i-1][j-k]
        arr = []
        for i in range(6*n):
            if d[n-1][i] != 0:
                arr.append(d[n-1][i]/pow(6,n))
        return arr
                