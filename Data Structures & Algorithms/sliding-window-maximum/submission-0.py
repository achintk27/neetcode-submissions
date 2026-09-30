class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #create a candidates variable to store indexes 
        candidates = deque()
        result = []

        #iterate through nums 
        for right in range(len(nums)) :

            #remove oldest candidate if its no longer inside window
            if candidates and candidates[0] <= right - k :
                candidates.popleft()
            
            while candidates and nums[candidates[-1]] <= nums[right] :
                candidates.pop()
            
            #if candidate is in the window 
            candidates.append(right)

            if right >= k -1 :
                result.append(nums[candidates[0]])

        return result







        