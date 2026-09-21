class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # we need to find a speed k which is the slowest speed in which she can finsih all bananas in the mentioned time 

        left = 1 
        right = max(piles)

        while left < right :
            speed = (left + right) // 2 

            hours = 0

            #iterate through the piles 
            for pile in piles :
                
                #hours per pile = (pile + speed - 1) // speed
                hours += (pile + speed - 1) // speed

            # this speed works , but lesser speed could work too 
            if hours <= h :
                right = speed 
            
            #speed is too slow 
            else :
                left = speed + 1 

        #smallest working speed     
        return left



