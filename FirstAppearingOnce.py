# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.arr = []
    def FirstAppearingOnce(self):
        if self.arr:
            return self.arr[0]
        else:
            return '#'
    def Insert(self, char):
        if char in self.arr:
            self.arr.remove(char)
        else:
            self.arr.append(char)