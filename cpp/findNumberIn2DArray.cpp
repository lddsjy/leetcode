class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        for(int i = 0; i<matrix.size();i++){
            for(int j = 0; j<matrix[i].size(); j++){
                if(target==matrix[i][j]) return true;
            }
            
        }
        return false;

    }
};

class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0) return NULL;
        int i=0,j=matrix[0].size()-1;
        while((i<matrix.size()) && (j>=0)){
            if(matrix[i][j]>target) j--;
            else if(matrix[i][j]<target) i++;
            else return true;
        }
        return false;

    }
};