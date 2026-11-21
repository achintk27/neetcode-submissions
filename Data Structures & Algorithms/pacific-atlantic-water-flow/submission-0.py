class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #define the rows and columns 
        rows = len(heights)
        cols = len(heights[0])


        # we create 2 sets to store whether water from this position can reach the atlantic or pacific
        pacific = set()
        atlantic = set()


        # bfs function here takes 2 attributs - 1. where we start , 2. is it reachable to this ocean. reachable is the set for the ocean we are searching from. eg : bfs(pacific_starts, pacific)
        def bfs(start_cells , reachable) :

            #create a queue that stores all the cells that can reach the ocean but whose neighbours are unchecked
            queue = deque()

            #initially add all oceanedge cells onto the queue since they can reach the ocean
            for row , col in start_cells : 
                if (row , col) not in reachable : 
                    reachable.add((row , col))
                    queue.append((row , col))
            

            #we need to check the 4 directions 
            directions = [ (1 , 0) , (-1 , 0) , (0 , 1), (0 , -1)]

            #while elements are in queue , pop the left most element 
            while queue :
                row , col = queue.popleft()


                #check if the new_row and new_col (i.e in the 4 directions) is existant
                for change_row , change_col in directions : 
                    next_row = row + change_row 
                    next_col = col + change_col


                    #check their existance 
                    if (next_row < 0 or next_row >= rows or 
                        next_col < 0 or next_col >= cols) :
                        continue 
                    

                    #check if we have already reached this neighnour 
                    if (next_row , next_col) in reachable : 
                        continue 
                    

                    # we check the neighbours backward 
                    if heights[next_row][next_col] < heights[row][col] :
                        continue 

                    
                    #if new_height is > old height we add this cell to that oceans reachable and then add to queue 
                    reachable.add((next_row , next_col))
                    queue.append((next_row , next_col))
            

            #create empty arrays for pacific and altantic in the start 
        pacific_start = []
        atlantic_start = []


        # add the left edge cells to pacific and right edge to atlantic 
        for row in range(rows) : 
            pacific_start.append((row , 0))
            atlantic_start.append((row , cols - 1))
            

        # add top edge to pacific and bottom edge atlantix 
        for col in range(cols) : 
            pacific_start.append((0 , col))
            atlantic_start.append((rows - 1 , col))

            
        #call bfs from these cells 
        bfs(pacific_start , pacific)
        bfs(atlantic_start , atlantic)


        result = []


        for row in range(rows) :
            for col in range(cols) :
                if (row , col) in pacific and (row , col) in atlantic :
                    result.append([row , col])
            

        return result 





                    























        