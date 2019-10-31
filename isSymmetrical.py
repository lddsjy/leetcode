# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True

        def isSame(p1,p2):
            if not p1 and not p2:
                return True
            if p1 and p2 and p1.val == p2.val:
                # 左边的左孩子等于右边的右孩子，左边的右孩子等于右边的左孩子
                return isSame(p1.left,p2.right) and isSame(p1.right,p2.left)
            else:
                return False
        return isSame(pRoot.left,pRoot.right)

t1= TreeNode(8)
t2= TreeNode(6)
t3= TreeNode(6)
t4= TreeNode(5)
t5= TreeNode(7)
t6= TreeNode(7)
t7= TreeNode(5)
t1.left=t2
t1.right=t3
t2.left=t4
t2.right=t5
t3.left=t6
t3.right=t7
s=Solution()
# s.mirrorTree(t1)
# print(t3.left.val,t3.right.val)
print(s.isSymmetrical(t1))