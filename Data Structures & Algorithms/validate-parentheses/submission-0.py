class Solution:
    def isValid(self, s: str) -> bool:
        
        #intuition : 
        # [
        #   (
        #     {

        #     }
        #   )  
        # ]

        # [ ( { } ) ] 

        # mainly need to determine if opening and closing brackets come in correct order
        # Opening bracket → save it

        # Closing bracket → make sure something was opened
        #                 → remove the latest opening bracket
        #                 → make sure the two brackets match

        # At the end → make sure nothing remains open

        stack = [] # empty stack that will have closing brackets 

        pairs = {  # closing brackets are keys to opening brackets
            ")" : "(",
            "}" : "{",
            "]" : "[" 
        }

        #traverse the string 
        for bracket in s :
            if bracket in pairs : # check if key is present in pairs for the bracket we are o 
                if not stack : # meaning it never had an opening bracket before closing
                    return False 
                

                opening = stack.pop() # variable storing the opening bracket 

                if opening != pairs[bracket] :# if the last opened bracket is not the key to the current closing bracket we are on 
                    return False  
                
            else :
                stack.append(bracket)
            
        return not stack # return true 
                     





