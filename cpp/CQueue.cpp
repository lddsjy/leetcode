class CQueue {
public:
    stack<int> s1;
    stack<int> s2;

    CQueue() {

    }
    
    void appendTail(int value) {
        s1.push(value);

    }
    
    int deleteHead() {
        if(!s2.empty()){
            int a = s2.top();
            s2.pop();
            return a;
        }
        else if(!s1.empty()){
            while(!s1.empty()){
                int a = s1.top();
                s2.push(a);
                s1.pop();
            }
            int a = s2.top();
            s2.pop(); 
            return a;            
        }
        else
            return -1;

    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */