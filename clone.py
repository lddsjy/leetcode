# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        pHeadRoot = pHead

        while(pHead):
            pHead1 = RandomListNode(pHead.label)
            pHead1.next = pHead.next
            pHead.next = pHead1
            pHead = pHead1.next
        pHead = pHeadRoot
        while(pHead):
            if pHead.random:
                pHead.next.random = pHead.random.next
            pHead = pHead.next.next
            #pHead1.next可能为空
            # pHead1= pHead1.next.next
        pHead = pHeadRoot
        pHead1 = pHead.next
        headCopy = pHead.next
        # pHead = pHead.next.next
        while(pHead1):
            if pHead1.next:
                pHead1.next = pHead1.next.next
            pHead1 = pHead1.next
        return headCopy

n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n4 = RandomListNode(4)
n5 = RandomListNode(5)
n1.next = n2
n1.random = n3
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
newHead=s.Clone(n1)
tmp = newHead
while tmp:
    print(tmp.label)
    if tmp.random:
        print(tmp.random.label)
    tmp=tmp.next