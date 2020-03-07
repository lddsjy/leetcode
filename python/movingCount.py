# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.count = 0
#     def movingCount(self, threshold, rows, cols):
#         arr = [[0]*cols]*rows
#         print(arr[1][3])
#         def over(r,c):
#             s=sum(map(int,str(r)+str(c)))
#             return s>threshold
#
#         def tranverse(r,c):
#             print('enter:',r,c,arr[r][c])
#             if not (0<=r<rows and 0<=c<cols):return
#             if over(r,c):
#                 arr[r][c] = -1
#                 return
#             if arr[r][c] != 0:
#                 return
#             self.count +=1
#             arr[r][c] = 1
#             print(r,c)
#             tranverse(r + 1, c)
#             tranverse(r - 1, c)
#             tranverse(r, c + 1)
#             tranverse(r, c - 1)
#         tranverse(0,0)
#         return self.count
class Solution:
    def __init__(self):
        self.count = 0
    def movingCount(self, threshold, rows, cols):
        # write code here
        board = [[0 for _ in range(cols)] for _ in range(rows)]
        def block(r,c):
            s = sum(map(int,str(r)+str(c)))
            return s>threshold
        def traverse(r,c):
            if not (0<=r<rows and 0<=c<cols): return
            if board[r][c]!=0: return
            if block(r,c):
                board[r][c]=-1
                return
            board[r][c] = 1
            self.count+=1
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c+1)
            traverse(r,c-1)
        traverse(0,0)
        return self.count
s = Solution()
print(s.movingCount(5,10,10))