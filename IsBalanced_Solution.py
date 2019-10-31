# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        if abs(self.Treedepth(pRoot.left)-self.Treedepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def Treedepth(self,root):
        if not root:
            return 0
        return max(self.Treedepth(root.left)+1,self.Treedepth(root.right)+1)