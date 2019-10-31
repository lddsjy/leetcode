# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        arr = []
        if not pRoot:
            return []
        arr.append([pRoot])
        arrOut = []
        order = 1
        while arr:
            ps = arr.pop(0)
            tmp = []
            for p in ps:
                if p.left:
                    tmp.append(p.left)
                if p.right:
                    tmp.append(p.right)
            if tmp:
                arr.append(tmp)
            if order == 1:
                arrOut.append([i.val for i in ps])
            if order == -1:
                arrOut.append([i.val for i in ps[::-1]])
            order = -order
        return arrOut
# class Solution:
#     def Print(self, pRoot):
#         arr = []
#         if not pRoot:
#             return None
#         arr.append([pRoot,-1])
#         arrOut = [pRoot.val]
#         while arr:
#             p,order = arr.pop(0)
#             if order == -1:
#                 if p.right:
#                     arrOut.append(p.right.val)
#                 if p.left:
#                     arrOut.append(p.left.val)
#                     arr.append([p.left,-order])
#                 if p.right:
#                     arr.append([p.right, -order])
#             if order == 1:
#                 if p.left:
#                     arrOut.append(p.left.val)
#                     arr.append([p.left,-order])
#                 if p.right:
#                     arrOut.append(p.right.val)
#                     arr.append([p.left,-order])
#         return arrOut
# class Solution:
#     def Print(self, pRoot):
#         # write code here
#         if not pRoot:
#             return []
#         from collections import deque
#         res,tmp=[],[]
#         last=pRoot
#         q=deque([pRoot])
#         left_to_right=True
#         while q:
#             t=q.popleft()
#             tmp.append(t.val)
#             if t.left:
#                 q.append(t.left)
#             if t.right:
#                 q.append(t.right)
#             if t == last:
#                 res.append(tmp if left_to_right else tmp[::-1])
#                 left_to_right= not left_to_right
#                 tmp=[]
#                 if q:last=q[-1]
#         return res
t1= TreeNode(8)
t2= TreeNode(10)
t3= TreeNode(6)
t4= TreeNode(5)
t5= TreeNode(7)
t6= TreeNode(9)
t7= TreeNode(11)
t1.left=t2
t1.right=t3
t2.left=t4
t2.right=t5
t3.left=t6
t3.right=t7
s=Solution()
print(s.Print(t1))