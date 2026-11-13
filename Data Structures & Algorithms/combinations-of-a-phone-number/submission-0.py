class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        #if 1 is chosen it has no letters associated
        if not digits :
            return []
        

        #store each of the number and its associated letters in a dictionary 
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }


        #have 2 arrays to store path and the result 
        result = []
        path = []


        #we backtrack using index which tells us which position are we choosing the char for 
        def backtrack(index) :

            #if the value of index = len of the digits then we have the required 2 or 3 .. chars 
            if index == len(digits) :
                
                #append the char substring into result 
                result.append("".join(path))
                return 


            #we also need a variable to chose all the alphabets associated with that number 
            #so if we have "23" where digits[0] = 2 ,  digits[1] = 3 
            # we need a variable that we can move along this to find all the char from the dictonary 
            current_digit = digits[index]

            #now we need to obtain all the alphabets for the current digit 
            for char in letters[current_digit] :
                path.append(char)

                #now we go to the next index 
                backtrack(index + 1)
                path.pop()
        
        backtrack(0)
        return result






        