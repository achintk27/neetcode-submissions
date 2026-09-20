class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0 
        right = len(heights) - 1
        largest = 0 
        
        for height in heights :

            while left < right :
                width = right - left 
                length = min(heights[left],heights[right])
                area = width * length

                largest = max(largest , area)


                if heights[left] <= heights[right] :
                    left +=1 
                
                elif heights[left] >= heights[right] :
                    right -=1
        
        return largest 


        