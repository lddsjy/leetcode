# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return None
        if not pRoot.left and not pRoot.right:
            return 1
        left=right = 0
        if pRoot.left:
            left = self.TreeDepth(pRoot.left)
        if pRoot.right:
            right = self.TreeDepth(pRoot.right)
        depth = 1+max(left,right)
        return depth

s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print(s.TreeDepth(t1))