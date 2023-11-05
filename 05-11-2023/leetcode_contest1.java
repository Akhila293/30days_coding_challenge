class Solution {
    public int findChampion(int[][] grid) {
        int c=0;
        int h=0,t=0;
        for(int i=0;i<grid.length;i++){
            c=0;
            for(int j=0;j<grid.length;j++){
                if(i!=j){
                    if(grid[i][j]==1)
                       c++; 
                }
            }
            if(c>h)
            {
                h=c;
                t=i;                
            }
        }
        return t;
    }
}