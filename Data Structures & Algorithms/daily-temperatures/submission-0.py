class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #create a satck filled with 0 , this will store the no of days and final ans 
        answer = [0] * len(temperatures)

        #create an empty stack 
        stack = []

        #enumerate the the temperatures , this stores current day(index) and current temp 
        for current_day , current_temp in enumerate(temperatures) :

            #when stack is not empty and current temp is greater than previous day , we get the number of days 
            while stack and current_temp > stack[-1][1] :

                #pop the previous day and previous temp 
                previous_day , previous_temp = stack.pop()

                #find the number of days between current day and previous day temp 
                answer[previous_day] = current_day - previous_day

            
            #input current day and current temp in stack 
            stack.append((current_day , current_temp))
        
        return answer



