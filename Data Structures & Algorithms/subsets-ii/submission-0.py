class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        #sort the elements so its easy to identify duplicates
        nums.sort()
        result = []
        path =[]

        def backtrack(start) :

            #whatever is in the path so far , is added to the result 
            result.append(path[:])

            for i in range(start , len(nums)) :

                #skip duplicates in that level , so it doesnt give same path 
                if i > start and nums[i] == nums[i - 1] :
                    continue 
                

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return result



        
        