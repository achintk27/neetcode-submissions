class Solution:
    def solve(self, board: List[List[str]]) -> None:

        #an " O " is surrounded if cant reach the edge by moving up , down , left or right through other " O " cells. 

        #we will first find every " O " on the edge , these are all safe so we mark them as " S". Any " O " connected to them arr also safe and marked " S". all remaining "O" are surrounded and marked "X".

        #first check if its an empty board
        if not board or not board[0] :
            return 

        rows = len(board)
        cols = len(board[0])


        #create an empty queue that stores the position of all the "O"
        queue = deque()

        #create a helper function that is used to convert all the "O" to "S"
        def add_to_safe(row , col) :
            if board[row][col] == "O" :
                board[row][col] = "S"

                # add to queue
                queue.append((row , col))
        

        # find the cells having "O" on left and right edges
        for row in range(rows) :
            
            #left edge
            add_to_safe(row , 0)

            #right edge
            add_to_safe(row , cols - 1)

        
        #find top and bottom edges 
        for col in range(cols) :

            #top edge
            add_to_safe(0 , col)

            #bottom edge
            add_to_safe(rows - 1 , col)

        

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #while we have cells that have "O" in the queue 
        while queue :
            row , col = queue.popleft()


            for change_row , change_col in directions : 
                next_row = row + change_row
                next_col = col + change_col


                #check if the next_row , next_col is existant 
                if (next_row < 0 or next_row >= rows or 
                    next_col < 0 or next_col >= cols) :
                    continue 
            

                add_to_safe(next_row , next_col)



        #find all surround "O"
        for row in range(rows) :
            for col in range(cols) :
                if board[row][col] == "O" :
                    board[row][col] = "X"
                
                elif board[row][col] == "S":
                    board[row][col] = "O"
        




               








        