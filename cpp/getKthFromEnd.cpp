class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode* newHead = head;
        int i = 0;
        while(i < k){
            head = head->next;
            i++;
        }
        while(head){
            head = head->next;
            newHead = newHead->next;
        }
        return newHead;

    }
};