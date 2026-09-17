class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # The numbers dont have to be in consecutive order in the given array

        # we start by adding all the numbers to a set
        # We start counting the length only if the previous number is not present in the list 
        # Eg : in the given array 1 is not present therefore 2 can be starting point. 
        # next we check if curr_number + 1 is present , if yes then current_length + 1 


        numbers = set(nums) 
        longest = 0

        # check if previous number is not there

        for number in numbers : 
            if number - 1 not in numbers :
                current_number = number 
                current_length = 1 

            
        # check if next number is present 

                while current_number + 1 in numbers :
                    current_number += 1
                    current_length += 1
            
                longest = max(longest , current_length)
        
        return longest



        