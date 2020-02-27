class Solution {
public:
    TreeNode* mirrorTree(TreeNode* root) {
        if(root){ 
            // TreeNode *treeNode = new TreeNode(preorder[0]);
            TreeNode *temp = new TreeNode(root->val);
            temp = root->left;
            root->left = root->right;
            root->right = temp;
            if(root->left) mirrorTree(root->left);
            if(root->right) mirrorTree(root->right);
            }
        return root;

    }
};