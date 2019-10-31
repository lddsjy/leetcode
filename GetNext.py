# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            left = pNode.right
            while left.left:
                left = left.left
            return left
        else:
            root = pNode.next
            while root:
                if root.left == pNode:
                    return root
                else:
                    pNode = root
                    root = root.next
            

