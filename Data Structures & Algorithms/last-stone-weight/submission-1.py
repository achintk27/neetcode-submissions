#we can use min heap , but make it act as max heap 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # every weight stored inside this heap must be negative , this makes the min heap remvove the heaviest real stone 
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
                
                #the remaning will be a +ve value so we use -ve sign 
                heapq.heappush(heap , -remaning)
        
        if heap :
            return -heap[0]
    
        return 0





        