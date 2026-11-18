class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        #similar problem compared to isalnds and chests

        #mentions what are the rows and cols to traverse later 
        rows = len(grid)
        cols = len(grid[0])

        #we will maintain a queue to store the location of all the rotten fruits in the begining 
        queue = deque()
        
        #count the number of frest fruits as well , its 0 initially 
        fresh = 0 


        #count the number of fresh fruits initally and also add the position of rotten fruits into the queue 
        for row in range(rows) :
            for col in range(cols) :

                #if we see a fresh fruit , inc count 
                if grid[row][col] == 1 :
                    fresh += 1 
                
                #if its rotten , add to queue 
                elif grid[row][col] == 2 :
                    
                    #maintain an extra variable time as well
                    queue.append((row , col , 0))
        

        #we will specify the 4 directions we the move & initially minutes = 0 
        directions = ((1 , 0), (-1 , 0) , (0 , 1), (0 , -1))
        minutes = 0 


        #pop the values of the rotten fruits from the queue 
        while queue : 
            row , col, time = queue.popleft() 

            #the (1 , 0), (-1 , 0) , (0 , 1) .. will be the values of change_row and change_col
            for change_row , change_col  in directions :
                next_row = row + change_row
                next_col = col + change_col


                #if the neighbour of thr rotten fruit is out of the grid or not fresh , we continue 
                if (next_row < 0 or next_row >= rows or 
                    next_col < 0 or next_col >= cols) :
                    continue 

                
                if grid[next_row][next_col] != 1 :
                    continue 
                

                #if it is fresh , it turns rotten and the number of fresh decreases 
                grid[next_row][next_col] = 2
                fresh -= 1

                #time increments by 1 
                next_time = time + 1 

                #the total mins is max of new time and minutes
                minutes = max(next_time , minutes)

                # add the new value to the queue
                queue.append((next_row , next_col , next_time))

    
        #if there is a chace that not all fruits can become rotten , return -1 
        if fresh > 0 : 
            return -1 

        
        return minutes 












                

        