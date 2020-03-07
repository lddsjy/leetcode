/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* nhead;
        if(!head) return nullptr;
        Node* begin = head;
        while(head){
            Node* nhead = new Node(head->val);
            Node* temp = head->next;
            head->next = nhead;
            nhead->next = temp;
            head = temp;          
        }
        head = begin;
        while(head){
            if(head->random) head->next->random = head->random->next;
            else head->next->random = NULL;
            head = head->next->next;
        }
        head = begin;
        nhead = begin->next;
        Node* r = nhead;
        while(head){
            head->next = head->next->next;
            if(nhead->next) nhead->next = nhead->next->next;
            else nhead->next = NULL;
            head = head->next;
            nhead = nhead->next;
        }
        return r;
    }
};