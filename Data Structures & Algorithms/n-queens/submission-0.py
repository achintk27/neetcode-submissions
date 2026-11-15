class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        #no 2 queens can be in same diagonal , row or column 
        #we need to find the 4 spots that make this possible - there is more than 1 solu
        #since we wan† all possible solutions we use backtracking , if we wanted a single solu we use dynamic programming 


        result = []

        #start will all the cells having "."
        board = [["."] * n for _ in range(n)]


        #we need a way to store all the used columns and diagonals. we go row by row 
        used_col = set() # set stores value in unordered way so we use it
        used_diagonal1 = set()
        used_diagonal2 = set()


        #we traverse row wise
        def backtrack(row):

            # a unique combination is got once all rows are filled 
            if row == n :
    
                #it joins all the cells in the line into a single string 
                completed = ["".join(line) for line in board]
                result.append(completed)
                return 

            
            # when we need to add the queen we check all columns in that row
            for col in range(n) :

                #define each diagonal. This is done because we dont want 2 elements in different rows to be in same diagonals 
                diagonal1 = row + col 
                diagonal2 = row - col


                #if that col or diagonal is used we skip that 
                if (col in used_col or
                    diagonal1 in used_diagonal1 or
                    diagonal2 in used_diagonal2) :
                    continue 
                

                #if its a valid pos , we insert Q at that cell and mark those col and diaginals as used 
                board[row][col] = "Q"
                used_col.add(col)
                used_diagonal1.add(diagonal1)
                used_diagonal2.add(diagonal2)


                #go to next row 
                backtrack(row+1)


                #once that combination is got , undo the operations and start for new combination
                board[row][col]="."
                used_col.remove(col)
                used_diagonal1.remove(diagonal1)
                used_diagonal2.remove(diagonal2)

        backtrack(0)
        return result
                









       

        




        