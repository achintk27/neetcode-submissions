class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #we use DFS here 
        #DFS - keep going till we hit a deadend , go back to the nearest exit point and then take a different route.
        
        row , col = len(grid) , len(grid[0])
        count = 0

        #Call DFS 
        def dfs(r , c) :

            #stop if we hit water , already visited island or out of grid
            # r < 0 - went off top edge , r >= row - went off bottom edge , c < 0 - went off left side , c >= col - went off right side.
            # grid[r][c] != "1" - water or already visited
            if r < 0 or r >=row or c < 0 or c >= col or grid[r][c] != "1" :
                return  
            
            #if not visited , mark " # " implying visited 
            grid[r][c] = "#"

            #perform dfs on all neighbours 
            dfs(r + 1 , c)
            dfs(r - 1 , c)
            dfs(r , c + 1)
            dfs(r , c - 1)
        
        #caliculate the count 
        for r in range(row) :
            for c in range(col) :
                if grid[r][c] == "1":
                    count += 1
                    dfs(r , c)
            
        return count 


