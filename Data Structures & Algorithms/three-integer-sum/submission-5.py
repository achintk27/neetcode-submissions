class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #sort the array in accending order 
        nums.sort()

        result = []

        #enum and store nums and index 
        for index , number in enumerate(nums) :

            if number > 0:
                break

            #skip duplicate nums first , so we dont get same triplets 
            #if number is = to previous number , skip 
            if index > 0 and number == nums[index - 1]:
                continue
                 

            # we begin left with immediate next number compared to what we are traversing
            left = index + 1

            #right is the last number 
            right = len(nums) - 1

            while left < right : 
                current_sum = number + nums[left] + nums[right]

                if current_sum < 0:

                    #since it is in increasing order left needs to be incremeneted  
                    left +=1 
                
                elif current_sum > 0 :
                    right -=1

                #append the triplet onto the result array 
                else :
                    result.append([number ,nums[left],nums[right]])

                
                    left+= 1
                    right -=1
                
                    #skip duplicate left values :
                    while left < right and nums[left] == nums[left - 1] :
                        left+=1
                
        return result

            



