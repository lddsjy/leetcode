class Solution {
public:
    vector<int> res;
    vector<int> reversePrint(ListNode* head) {
        while(head){
            res.push_back(head->val);
            head = head->next;
            
        }
        reverse(res.begin(),res.end());
        return res;


    }
};

class Solution {
public:
    vector<int> res;
    stack<int> s;
    vector<int> reversePrint(ListNode* head) {
        while(head){
            s.push(head->val);
            head = head->next;
            
        }
        while(!s.empty()){
            res.push_back(s.top());
            s.pop();
        }
        return res;


    }
};