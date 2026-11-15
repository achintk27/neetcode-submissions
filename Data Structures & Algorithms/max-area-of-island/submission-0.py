class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        #Both DFS and BFS are fine 
        #once we find a 1 , we need to check if that cell is an island on its own or are there connecting islands. We can run DFS on all 4 directions. 
        #if there is water or its out of bounds , the dfs return 0. 
        #we can change the value of cell from 1 to 0 to mark visited 
        #we run dfs on all the islands to find which has the max area. 


        rows = len(grid)
        cols = len(grid[0])
        
        #initially the area of the largest island is 0
        largest = 0 


        def dfs(row , col) :

            # if we are out of bounds or its water , return 0  
            if(row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0) :
                return 0  

            
            #if the cell has a 1 , we inc the area count and change the value to 0 so that its marked visited 
            grid[row][col] = 0 
            area = 1


            # perform DFS on all 4 sides
            area += dfs(row + 1 , col)
            area += dfs(row - 1 , col)
            area += dfs(row , col + 1)
            area += dfs(row , col - 1)
           
            return area 
        

        # the loop is we check every value of the matrix : O(n * m)
        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] == 1 :
                    largest = max(largest , dfs(row , col))
        

        return largest 








            





        