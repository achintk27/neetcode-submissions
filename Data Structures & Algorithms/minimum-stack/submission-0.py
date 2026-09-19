class MinStack:

    def __init__(self):
        #create 2 stacks 

        #stores every value 
        self.stack = []

        #stores minimum value 
        self.min_stack = []

        

    def push(self, val: int) -> None:

        #push every value to stack 
        self.stack.append(val)

        #push to min_stack if min_stack is empty or val is less than current minimum (i.e top element of min_stack)
        if not self.min_stack or val <= self.min_stack[-1] :
            self.min_stack.append(val)

        
    def pop(self) -> None:

        #remove and save the tope element as value 
        value = self.stack.pop()

        #pop from min_stack if value is top most (least) element in min_stack 
        if value == self.min_stack[-1] :
             self.min_stack.pop()
   

    def top(self) -> int:

        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]
        
