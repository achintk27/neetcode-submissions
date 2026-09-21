class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1 

        while left <= right :
            middle = (left + right) // 2 

            if nums[middle] == target :
                return middle 
            
            # we check if left half is sorted 
            if nums[left] <= nums[middle] :

                # we check if the target is towards the left or right of middle
                if nums[left] <= target < nums[middle] :
                    right = middle - 1 
                
                else:
                    left = middle + 1
            
            # else the right half is sorted 
            else :
                
                #check if target is to the right of middle 
                if nums[middle] < target <= nums[right] :
                    left = middle + 1 
                
                else:
                    right = middle - 1 
        
        return -1 






        