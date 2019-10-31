# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        arr = []
        arr = self.minnode(pRoot,arr)
        print(arr)
        if k<=len(arr) and k>0:
            return arr[k-1]
        else:
            return None
    def minnode(self,pRoot,arr):
        if not pRoot:
            return None
        self.minnode(pRoot.left,arr)
        arr.append(pRoot.val)
        self.minnode(pRoot.right,arr)
        return arr
# class Solution:
#     # 返回对应节点TreeNode
#     def KthNode(self, pRoot, k):
#         if not pRoot:
#             return None
#         arr = [pRoot]
#         arrOut = [pRoot.val]
#         while arr:
#             p = arr.pop(0)
#             if p.left:
#                 arr.append(p.left)
#                 arrOut.append(p.left.val)
#             if p.right:
#                 arr.append(p.right)
#                 arrOut.append(p.right.val)
#         arrOut = sorted(arrOut)
#         if k>len(arrOut) or k<1:
#             return None
#         return arrOut[k-1]
t1= TreeNode(8)
t2= TreeNode(6)
t3= TreeNode(10)
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
print(s.KthNode(t1,0))