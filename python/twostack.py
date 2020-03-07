# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.acceptstack = []
        self.outputstack = []
    def push(self, node):
        # write code here
        self.acceptstack.append(node)
    def pop(self):
        if self.outputstack:
            return self.outputstack.pop()
        elif self.acceptstack:
            while self.acceptstack:
                self.outputstack.append(self.acceptstack.pop())
            return self.outputstack.pop()
        else:
            return None