# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minN = []
    def push(self, node):
        self.stack.append(node)
        if self.minN and self.minN[-1] < node:
            self.minN.append(self.minN[-1])
        else:
            self.minN.append(node)
    def pop(self):
        if not self.stack:
            return None
        else:
            self.minN.pop()
            self.stack.pop()
            return self.stack
    #def top(self):
        # write code here
    def min(self):
        if self.minN:
            return self.minN[-1]
        else:
            return None