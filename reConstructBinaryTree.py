# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        if len(pre) != len(tin):
            return None
        root = pre[0]
        print(root)
        rootNode = TreeNode(root)

        ind = tin.index(root)
        print(ind)
        tinLeft = tin[:ind]
        tinRight = tin[ind+1:]
        preLeft = pre[1:ind+1]
        preRight = pre[ind+1:]

        leftNode = self.reConstructBinaryTree(preLeft,tinLeft)
        rightNode = self.reConstructBinaryTree(preRight,tinRight)
        if leftNode:
            rootNode.left = leftNode
        if rightNode:
            rootNode.right = rightNode

        return rootNode

s = Solution()
print(s.reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7]))