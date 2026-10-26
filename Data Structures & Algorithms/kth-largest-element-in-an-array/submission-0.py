class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #create a min heap with the kth largest elemnet at the root 
        #use heapq.heappush and create a min heap
        #Build the heap only until k elements , so that the kth largest element will always be at the root 
        heap = []

        #iterate through the array , create a heap having k elements 
        for num in nums : 
            
            #this would mean that the kth largest element so far is at the root 
            if len(heap) < k :
                heapq.heappush(heap ,num)
            
            #if the heap is of size k , check if the num now is > root
            elif num > heap[0]:
                heapq.heapreplace(heap , num)
            
        return heap[0]


        