class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #find 2 nos where num on right - num of left is largest 

        lowest = prices[0]
        largest_profit = 0 

        for day in range(1,len(prices)):
            price = prices[day]
            profit = price - lowest


            #This creates the sliding windows 
            largest_profit = max(largest_profit , profit)
            lowest = min(lowest , price)

        return largest_profit