# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        #注意这里是and
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        self.Convert(pRootOfTree.left)
        #连接左子树和根节点
        left = pRootOfTree.left
        if left:
            while left.right:
                left = left.right
        # 左子树最右和根节点相互连接
            left.right,pRootOfTree.left = pRootOfTree,left

        self.Convert(pRootOfTree.right)
        #连接右子树和根节点
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
        #右子树最左和根节点相互连接
            right.left,pRootOfTree.right = pRootOfTree,right

        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
s = Solution()
t1 = TreeNode(10)
t2 = TreeNode(6)
t3 = TreeNode(14)
t4 = TreeNode(4)
t5 = TreeNode(8)
t6 = TreeNode(12)
t7 = TreeNode(16)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7

root = s.Convert(t1)
print(root.val)
while root:
    print('*'*5)
    print(root.val)
    if root.left:
        print("left:",root.left.val)
    if root.right:
        print("right:",root.right.val)
    root = root.right