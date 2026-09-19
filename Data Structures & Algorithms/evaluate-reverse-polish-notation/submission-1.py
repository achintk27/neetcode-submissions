class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

    # create an empty stack 
        stack = []

        #mention the operators :
        operators = {"+","-","*","/"}

        #traverse the string
        for token in tokens :

            #check if the token is an interger (number)
            if token not in operators :

                # add the integer to the stack
                stack.append(int(token))

            #if it is an operator , pop 2 numbers 
            else:
                right = stack.pop()
                left = stack.pop()
            
                if token == "+" :
                    stack.append(right+left)
                
                elif token == "-" :
                    stack.append(left - right)
                
                elif token == "*" :
                    stack.append(left*right)
                
                else:
                    stack.append(int(left/right))
                
        return stack[-1]
                




