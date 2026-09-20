class Solution:
    def trap(self, height: List[int]) -> int:
        
        #left max = tellest left from 0 to i 
        #right max = tallest from len(num)-1 to i 

        if not height :
            return 0
        
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        #2 pointers move if left < right 
        while left < right :

            #check if h[left] < h[right]
            if height[left] < height[right] :

                #check if this left > left max 
                if height[left] >= left_max :
                    left_max = height[left] 
                
                #caliculate the amount of water
                else:
                    water += left_max - height[left]
                
                left+= 1
            
            #if h[right] < h[left]
            else:

                #check if h[right] > right_max
                if height[right] >= right_max :
                    right_max = height[right]
                
                else:
                    water += right_max - height[right] 
                
                right-= 1
        
        return water


