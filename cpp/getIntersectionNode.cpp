class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* node1 = headA;
        ListNode* node2 = headB;
        
        while(node1 != node2){
            if(node1 != NULL) node1 = node1->next;
            else node1 = headB;
            if(node2 != NULL) node2 = node2->next;
            else node2 = headA;
            
        }
        return node1;
        
    }
};


// class Solution {
// public:
//     ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
//         ListNode *node1 = headA;
//         ListNode *node2 = headB;
        
//         while (node1 != node2) {
//             node1 = node1 != NULL ? node1->next : headB;
//             node2 = node2 != NULL ? node2->next : headA;
//         }
//         return node1;
//     }
// };
