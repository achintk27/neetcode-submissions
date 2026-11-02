class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #create 2 arrays to store path so far and the final result 

        result = []
        path = []

        def backtrack(start , remaining):

            #after we insert a value into path , check if remaining = 0
            if remaining == 0 :
                result.append(path[:])
            
            #check if we have gone overboard
            if remaining < 0 :
                return 
            

            #the way we get the elements is by iterating through nums
            #rule : a number can be used multiple times 
            for i in range(start , len(nums)) :

                # add the value to path 
                path.append(nums[i])

                #backtrack to find other numbers , start with i cause same number can be used multiple times 
                backtrack(i , remaining - nums[i])

                #if the path does not lead to target 
                path.pop()
            
        backtrack(0 , target)
        return result 





        