class Solution {
public:
    int add(int a, int b) {
        vector<int> arr;
        arr = {a,b};
        return std::accumulate(arr.begin(),arr.end(),0);
        
    	// vector<int> v = {a,b};
    	// return std::accumulate(v.begin(), v.end(), 0);

    }
};

class Solution {
public:
    int add(int a, int b) {
 while(b)
        {
            int temp = a ^ b;
            // 注意leetcode中C++无法对int型最小值进行左移（所以转为无符号int型）
            b = (unsigned int)(a & b) << 1;
            a = temp;
        }
        return a;
    }
};