class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #sort the cars by postion and speed from largest to smallest 
        #zip the position and speed , e.r : ((position , speed), (position,speed))

        #reverse = True for largest to smallet
        cars = sorted(zip(position , speed), reverse = True)

        #create an empty stack 
        stack = []

        #caliculate the time it for take to reach target for each car 
        for car_position , car_speed in cars :
            time = (target - car_position) / car_speed

            #we store the value of fleets , i.e time it takes to reach in stack 
            if not stack or time > stack[-1] :

                #creates a new fleet
                stack.append(time)
        
        return len(stack)
            





        