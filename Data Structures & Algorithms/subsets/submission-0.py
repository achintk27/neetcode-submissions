class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #intuition : use backtracking 
        #at each num , we store the subset. We see what else can be added to this now.

        #use an array that stores the path. All nodes so far 
        path = []

        #array to store final solu : 
        result = []

        #begin backtracking from the root 
        def backtrack(start) :

            # add all the subarrays in the path to result 
            #this is written before the append , because we need empty array also in the solu 
            result.append(path[:])

            #first add the elemnt onto the path 
            for i in range(start , len(nums)): 
                path.append(nums[i])

                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return result



