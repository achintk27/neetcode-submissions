class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        #for every cell we want the fewest moves to the chest 
        #we use BFS because we it can traverse every cell based on the distance 

        #check if there are no rows or that the 1st row has no elements 
        if not grid or not grid[0] :
            return 
        

        #define what are rows , cols and INF 
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        # we will store the positions of all the chests in queue. Based on their distances from he begining. Initially maintain an empty queue 
        queue = deque()

        # add all he chests into the queue 
        for row in range(rows) :
            for col in range(cols) :

                #if the cell is a chest , add to the queue 
                if grid[row][col] == 0 :
                    queue.append((row , col))
            

        #next we define the directions in which we can move. we start from the chest that was discovered 1st , and check all for directions. if the cell is a land we ca traverse we caliculate the distance to the chest. 
        directions = [(1 , 0) , (-1 , 0), (0 , -1), (0 , 1)]


        #while we have chest in the queue we iterate to find distances
        while queue :

            # pop the elements in the queue from the left (the earliest 1st) and this becomes our current row and col. We check all the 4 directions now 
            row, col = queue.popleft()
            

            #change row and change_col assumes values of ( 1 , 0 ) , (-1 , 0)... respectively ( all 4 possible values)
            for change_row , change_col in directions : 
                next_row = row + change_row
                next_col = col + change_col


                #if the value in the new cell is not a land or we are out of the grid , continue 
                if (next_row < 0 or next_row >= rows or 
                    next_col < 0 or next_col >= cols) :
                    continue 

                
                if (grid[next_row][next_col] != INF ) :
                    continue 
                

                #if the value in the new cell is land that can be traversed them we replace the current value with 1 more than that.  
                grid[next_row][next_col] = grid[row][col] + 1
                queue.append((next_row , next_col))
                






        
        





        
        