# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        pHeadCopy = pHead
        temp = []
        while pHead:
            if pHead in temp:
                return pHead
            temp.append(pHead)
            pHead = pHead.next

