class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums) # create an array with 1's of length nums 

        #We solve this using prefix and suffix 

        #1. Prefix : calculate product of all nums before i
        prefix = 1
        for i in range(len(nums)) :
            output[i] = prefix
            prefix *= nums[i]

        
        #2. siffix : calculte product of all nums after i

        suffix = 1 
        for i in range(len(nums)-1, -1, -1): #start from the last 
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
        
        