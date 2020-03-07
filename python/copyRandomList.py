"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        begin = head
        while head:
            nhead = Node(head.val)
            temp = head.next
            head.next = nhead
            nhead.next = temp
            head = temp
        head = begin
        while head:
            head.next.random = head.random.next if head.random else None
            head = head.next.next
        head = begin
        nhead = begin.next
        r = nhead
        while head:
            head.next = head.next.next
            nhead.next = nhead.next.next if nhead.next else None
            head = head.next
            nhead = nhead.next
        return r
