class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # need to work using 1 based indexing

        # we use 2 pointers 1 at begining and 1 in the end

        left = 0 
        right = len(numbers) - 1 

        while left < right :

            #caliculate the sum 
            current_sum = numbers[left] + numbers[right]

            #if the current sum = target , return the indexs 
            if current_sum == target :
                return [left + 1 , right + 1]
            
            #if sum < target , since its in increasing order : left +=1 
            if current_sum < target : 
                left += 1
            
            elif current_sum > target : 
                right -= 1
            
        return current_sum 

        