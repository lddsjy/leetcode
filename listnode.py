#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        ret = []
        while listNode:
            ret.append(listNode.val)
            listNode = listNode.next
        return ret[::-1]

        # r = []
        # p = listNode
        # while p:
        #     r.append(p.val)
        #     p = p.next
        # #print(len(r))
        # return r[::-1]

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p1.next = p2
p2.next = p3

b=Solution()
print(b.printListFromTailToHead({}))