class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        newHead = head
        for _ in range(k):
            head = head.next
        
        while head:
            head = head.next
            newHead = newHead.next
        return newHead
            