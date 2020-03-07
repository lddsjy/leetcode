# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        strs = []
        if not root:
            return '#'
        strs.append(str(root.val))
        strs.append(self.Serialize(root.left))
        strs.append(self.Serialize(root.right))
        return ','.join(strs)

    def Deserialize(self, s):
        s = s.split(',')
        return self.my_de(s)
    def my_de(self,s):
        if len(s) == 0:
            return None
        leaf = s.pop(0)
        if leaf == "#":
            return None
        pRoot = TreeNode(int(leaf))
        pRoot.left = self.my_de(s)
        pRoot.right = self.my_de(s)
        return pRoot

s = Solution()
print(s.Deserialize('8,6,10,5,7,9,11').val)