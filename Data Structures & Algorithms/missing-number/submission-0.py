class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #use sum of n natural nos formula 

        n = len(nums)

        expected = n * (n + 1) // 2 
        actual = sum(nums)

        missing = expected - actual 

        return missing 
        