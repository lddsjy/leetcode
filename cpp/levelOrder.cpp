class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
        vector<int>res;
        if(root==NULL) return res;
        vector<TreeNode*> q;
        q.push_back(root);
        while(q.size()>0){
            root = q[0];
            res.push_back(root->val);
            q.erase(q.begin());
            if(root->left!=NULL) q.push_back(root->left);
            if(root->right!=NULL) q.push_back(root->right);
            
            
        }
        return res;
        

    }
};

class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
    	vector<int> nodes_levelorder;
    	if(!root) return nodes_levelorder;
    	nodes_levelorder.push_back(root->val);
    	list<TreeNode*> _list;
    	_list.push_back(root);
    	while(_list.size()){
    		//for debug
//    		TraverseTreeNodeList(_list);
    		if(root->left){
    			_list.push_back(root->left);
    		}
    		if(root->right){
    			_list.push_back(root->right);
    		}
    		_list.pop_front();
    		if(_list.size()){
        		root = _list.front();
        		nodes_levelorder.push_back(root->val);
    		}
    	}
    	return nodes_levelorder;
    }
};

作者：user2473E
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/solution/yin-ru-list-by-user2473e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。