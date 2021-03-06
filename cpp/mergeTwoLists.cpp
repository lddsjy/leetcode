/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* l = new ListNode(0) ;
        ListNode* r = l;
        while(l1 and l2){
            if(l1->val < l2->val){
                l->next = l1;
                l1 = l1->next;
            }else{
                l->next = l2;
                l2 = l2->next;                    
            }
            l = l->next;                       
        }
        if(l1) l->next = l1;
        if(l2) l->next = l2;
        return r->next;
        

    }
};