class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        path = []


        def backtrack(open_count , close_count) :

            #array is complete if len of string = 2 * n
            if len(path) == 2 * n :

                result.append("".join(path))

            
            # we need to add opening bracked if open_count < n 
            if open_count < n : 
                path.append("(")

                #backtrack with updated count
                backtrack(open_count + 1 , close_count)
                path.pop()
            

            #we need to add close bracket if close_count < open_count
            if close_count < open_count : 
                path.append(")")

                #backtrack with updated count 
                backtrack(open_count , close_count + 1)
                path.pop()
            

        backtrack(0 , 0)
        return result

    


        