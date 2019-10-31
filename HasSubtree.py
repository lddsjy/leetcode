# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.isSubtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

    def isSubtree(self,a,b):
        if not b:
            return True
        if not a or a.val != b.val:
            return False
        return self.isSubtree(a.left,b.left) and self.isSubtree(a.right,b.right)