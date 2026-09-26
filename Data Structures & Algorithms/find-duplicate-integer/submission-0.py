class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # we use cycle detection method and each number as index to visit next 
        # this helps in solving in O(n) and no modification to array 

        # 0 ---> 1 --- > 2 --- > 3 ---- > 2 ---- > 3 
        # here we see index 0 points to 1 , index 1 to 2 , index 2 points to 3 , index 3 to 2 ... cycle is formeed 

        slow = 0 
        fast = 0 

        # first we find where they meet in the cycle first. 
        while True :
            
            slow = nums[slow]
            
            #index points to what?
            fast = nums[nums[fast]]

            if slow == fast :
                break 

        #find entrance to the cycle 

        start = 0 
        while start != slow :
            start = nums[start]
            slow = nums[slow]
        
        return start
        
        