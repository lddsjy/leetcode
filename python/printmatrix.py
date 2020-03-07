# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        ret = []
        start = 0
        rows = len(matrix)
        cols = len(matrix[0] if matrix else 0)
        print(cols)
        while start*2 < rows and start*2 <cols:
            self.print_circle(matrix,start,rows,cols,ret)
            start += 1
        return ret

    def print_circle(self,matrix,start,rows,cols,ret):
        row = rows - start -1
        col = cols - start -1
        # left->right
        for c in range(start, col+1):
            ret.append(matrix[start][c])
        # top->bottom:
        if start < row:
            for r in range(start+1,row+1):
                ret.append(matrix[r][col])
        # right -> left
        if start < row and start < col:
            for c in range(start,col)[::-1]:
                ret.append(matrix[row][c])
        # bottom -> top:
        if start < row and start < col:
            for r in range(start+1, row)[::-1]:
                ret.append(matrix[r][start])
# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def __init__(self):
#         self.output = []
#     def printMatrix(self, matrix):
#         if matrix[0] == []:
#             return []
#         row = len(matrix)
#         col = len(matrix[0])
#         if col == 1:
#             for i in range(row):
#                 self.output.append(matrix[i][0])
#             return self.output
#         if row == 1:
#             return matrix
#         for i in range(col):
#             self.output.append(matrix[0][i])
#         for i in range(1,row):
#             self.output.append(matrix[i][col-1])
#         for i in range(col-2,-1,-1):
#             self.output.append(matrix[row-1][i])
#         for i in range(row-2,0,-1):
#             self.output.append(matrix[i][0])
#         #matrix = self.deleteMatrix(matrix)
#         matrix = matrix[1:row-1]
#         matrix= [matrix[i][1:col-1] for i in range(len(matrix))]
#         print(matrix)
#         self.printMatrix(matrix)
#         return self.output

s = Solution()
out = s.printMatrix([[]])

print('out=',out)