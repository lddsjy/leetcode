class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        
        while node1 != node2:
        #无公共节点就会在None处相遇
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1