#use min heap , cause heap[0] is always the smallest number
#at all times keep only the 3 largest numbers seen so far

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        
        #create a heap 
        self.heap = nums[:]

        #turn the heap into min heap
        heapq.heapify(self.heap)

        #discard smallest num until k elements remain
        while len(self.heap) > k :
            
            #since its a min heap it removes all values from the top
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:

        # add elements 
        heapq.heappush(self.heap , val)

        #make sure only required no of elements are there in the heap 
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        #now we have only k elements left , and as the lowest will be the root , return [0]
        return self.heap[0]
        



        
