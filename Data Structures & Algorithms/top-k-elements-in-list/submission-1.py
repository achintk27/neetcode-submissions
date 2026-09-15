class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = { } #hashmap to store each number and the count , each number = key , frquency = value 

        # we use bucket sort , buck is just a list
        for i in nums:
            count[i] = count.get(i , 0) + 1 # this returns the count of number. return the count of number if the number is present in the hash , else returns 0. adds 1 to it to update the count 

        bucket = [[] for _ in range(len(nums)+ 1)] # A number can appear at most len(nums) times.

        for i , frequency in count.items() :
            bucket[frequency].append(i) # we fill the frequency bucket for each index / number 


        result = []
        for frequency in range(len(nums), 0 , -1) : # start backward
            for i in bucket[frequency] :
                result.append(i)

                if len(result) == k :
                    return result


# idea : buckets index stores the count and bucket stores the number 

        