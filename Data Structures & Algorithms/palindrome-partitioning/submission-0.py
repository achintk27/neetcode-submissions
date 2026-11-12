class Solution:
    def partition(self, s: str) -> List[List[str]]:

        #create 2 arrays to hold substring(paths) and the result 
        result = []
        path = []

        def is_palindrome(substring) :

            #check if it is a palindrome
            return substring == substring[::-1]
        
        def backtrack(start):

            #each cycle checks all the possible cuts
            if start == len(s):
                result.append(path[:])
                return 
        
            for end in range(start+1 ,len(s)+1):

                #each piece includes start value and ends 1 pos behind end , so dont include end 
                #this includes start and not end , so 1st cut will be only ["a"] next it backtracks and takes [1:2] = ["a"] then ["b"] since all are pallindromes , start moves till end and we then append to result
                piece = s[start:end]
                if is_palindrome(piece) :
                    path.append(piece)
                    backtrack(end)
                    path.pop()
            
        backtrack(0)
        return result



        