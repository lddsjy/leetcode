class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        if(grid.size()==0 and grid[0].size()==0)
            return NULL;
        int i = 0, j = 0;
        for(i = 1; i< grid[0].size(); i++){
            grid[0][i] += grid[0][i-1];
        }
        for(i = 1; i<grid.size();i++){
            grid[i][0] += grid[i-1][0];
        }
        for(i = 1; i<grid.size();i++){
            for(j = 1; j<grid[0].size(); j++){
                grid[i][j] = max(grid[i-1][j],grid[i][j-1])+grid[i][j];
            }
        }
        return grid[grid.size()-1][grid[0].size()-1];

    }
};