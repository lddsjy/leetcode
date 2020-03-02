class Solution {
public:
    ListNode* deleteNode(ListNode* head, int val) {
        ListNode* pre = head;
        if(head->val == val) return head->next;
        ListNode* r = head;
        while(head){
            ListNode* after = head->next;
            if(head->val == val){
                pre->next = after;
            }
            pre = head;
            head = head->next;
            
        }
        return r;

    }
};