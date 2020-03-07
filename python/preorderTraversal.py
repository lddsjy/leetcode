# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.arr = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        self.arr.append(root.val)
        self.arr.append(self.preorderTraversal(root.left))
        self.arr.append(self.preorderTraversal(root.right))


s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(None)
t3 = TreeNode(2)
t4 = TreeNode(3)
t1.left = t2
t1.right = t3
t2.left = t4
print(s.TreeDepth(t1))
tmp.append(i.left) if i.left else None