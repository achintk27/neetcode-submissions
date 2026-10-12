#we can use min heap , but make it act as max heap 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # min heap would remove smallest val , since we want to remove the heavier one , we use -ve
        heap = [-weight for weight in stones] 
        
        #heapq creates a min heap
        heapq.heapify(heap)

        while len(heap) > 1 :
            
            #heaviest should be reduced 
            heaviest = -heapq.heappop(heap)
            second_heaviest = -heapq.heappop(heap)

            #if the two are not equal 
            if heaviest != second_heaviest :
                remaning = heaviest - second_heaviest
                
                
                heapq.heappush(heap , -remaning)
        
        if heap :
            return -heap[0]
    
        return 0





        