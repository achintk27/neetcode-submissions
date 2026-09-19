class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #create an empty stack 
        stack = []

        #initialise largest to 0 
        largest = 0 

        #store index and height for each 
        for index , height in enumerate(heights) :
            start = index 

            #if current height is > prev height then max height of rectangle is prev height 
            while stack and stack[-1][1] > height :

                #max height of rectange is prev height 
                previous_start , previous_height = stack.pop()

                #width = index - prev_index 
                width = index - previous_start

                area = width * previous_height 
                largest = max(largest, area)

                start = previous_start

            #if current height < previous height
            stack.append((start,height))

        # we now have the stack of the rectangle 
        for start , height in stack :
            width = len(heights) - start

            area = width * height
            largest = max(largest,area)
        
        return largest






