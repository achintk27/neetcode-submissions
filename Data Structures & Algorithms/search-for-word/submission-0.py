class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #Idea : try every cell as starting point , backtack to all neighbours. If we find all and run out of the letter , return True 
        row , col = len(board), len(board[0])

        #we use a 3rd vaiable k while backtracking , k tells us which letter of the word are we looking for now. word[0] , word[1]  ......
        def backtrack(r , c , k) :

            #if we go through all the letters then true 
            if k == len(word) :
                return True
            

            #return if we run of out space , visit a previously visited position or the letter is not present 
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[k] :
                return False 
            
            #if the correct letter is present , then store the actual letter from the matrix in temp and store # marking visited in the matrix
            temp = board[r][c]
            board[r][c] = "#"
            

            # if we find the correct letter then we need to backtrack and check all 4 neighnours. we can use a variable found which will store bool and perform backtrack
            found =(backtrack(r + 1 , c, k + 1) or 
                    backtrack(r - 1 , c, k + 1) or
                    backtrack(r , c + 1, k + 1) or 
                    backtrack(r , c - 1, k + 1)) 
            

            #once done , unmark the visited spot and store the actual value again 
            board[r][c] = temp
            return found 
        
        for r in range(row) :
            for c in range(col) :
                if backtrack(r , c , 0) :
                    return True 
        
        return False 







        