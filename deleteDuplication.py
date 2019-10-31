# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if (not pHead) or (not pHead.next):
            return None
        p = pHead
        pHead1 = pHead.next
        if pHead1.val != pHead.val:
            print('**',pHead1.val)
            pHead.next=self.deleteDuplication(pHead1)
        else:
            tmp = pHead1.next
            #print('tmp=',tmp.val)
            if tmp:
                pHead=self.deleteDuplication(tmp)
            else:
                return None
        return pHead
p0 = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(4)
p6 = ListNode(5)
p0.next=p1
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=p5
p5.next=p6

s = Solution()
p = p0
s.deleteDuplication(p0)
while p:
    print(p.val)
    p = p.next