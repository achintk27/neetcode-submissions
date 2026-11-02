class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        path = []

        #create an array that stores False for all values , we change this to true when we use it 
        used = [False] * len(nums)

        #we use backtrack
        def backtrack() :

            #check if the len of the path == len of nums 
            if len(path) == len(nums) :
                result.append(path[:])
                return

            
            for i in range(len(nums)) :

                #check if the number is used 
                if used[i] == True :
                    continue 
                
                #change false to used and add to path
                used[i] = True
                path.append(nums[i])
                backtrack()

                #once it reaches the max , tests all combinations for that loop
                path.pop()
                used[i] = False 
        
        backtrack()
        return result



