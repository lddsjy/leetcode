# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not path:
            return False
        #初始所有路径未走过
        flag = [[False for _ in range(cols)] for _ in range(rows)]
        #矩阵重排成二维
        matrix2D = [[matrix[i] for i in range(k*cols,(k+1)*cols)] for k in range(rows)]
        #path = list(path)
        result = False
        def route(r,c,path):
            if not (0<=r<rows and 0<=c<cols): return False
            if matrix2D[r][c] != path[0]:return False
            if flag[r][c]:return False
            print(r,c)
            flag[r][c] = True
            if len(path) == 1:
                print(path)
                return True
            return route(r+1,c,path[1:]) or route(r-1,c,path[1:]) or route(r,c+1,path[1:]) or route(r,c-1,path[1:])
        for i in range(rows):
            for j in range(cols):
                flag = [[False for _ in range(cols)] for _ in range(rows)]
                result = route(i,j,path)
                if result:
                    return True
        return result

s = Solution()
print(s.hasPath("ABCESFCSADEE",3,4,"ABCCED"))
