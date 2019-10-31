# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            print([[root.val]])
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        #print(left+right)
        for i in left+right:
            res.append([root.val]+i)
        return res

s = Solution()
t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(12)
t4 = TreeNode(4)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
print(s.FindPath(t1,22))