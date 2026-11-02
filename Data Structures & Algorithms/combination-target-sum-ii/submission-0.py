class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        #here we cant use duplicates , so we sort the elements such that duplicates are next to each other 
        candidates.sort()
        path = []
        result = []

        def backtrack(start , remaining) :

            # check if the remaining = 0 , to see if we found a path
            if remaining == 0 :
                result.append(path[:])
            
            #iterate through nums 
            for i in range(start , len(candidates)) :

                #since its sorted , if nums[i] > remaining , all elements after are also greater 
                if candidates[i] > remaining : 
                    break 

                #now check if the value i == previos value , if it does skip that in this level as it will lead to same path 
                if i > start and candidates[i] == candidates[i - 1] :
                    continue 
                

                #elese add the value i to path
                path.append(candidates[i])

                #backtrack starting from i + 1 , cause we cant use same element twice 
                backtrack(i + 1, remaining - candidates[i])

                #if the path is not equal to target , we pop it 
                path.pop()

                
        backtrack(0 , target)
        return result 
                




        