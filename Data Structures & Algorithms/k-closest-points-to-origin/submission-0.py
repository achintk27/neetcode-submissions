class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #we create a max heap , such that the farthest point is the root. Now if new element is < the root replace the root
        #python's heapq anyways implements a min heap - use this and store value in -ve 
        #now since we want the root to be the farthest point and its a min heap , we store the nums as negative numbers

        heap = []

        #for each pair caliculate the distance from the origin 
        for x , y in points :
            
            #no need of root cause cause greater the value , taking a root doesnt change that 
            distance = (x * x) + (y * y)

            #create a heap of size k 
            if len(heap) < k :
                
                #tuple adds based on 1st value , so it will add based on -distance onto the heap 
                heapq.heappush(heap ,(-distance , x , y))
            
            #if heap >= k , check if new element is nearer than farthest element , so compare with root 
            elif distance < -heap[0][0] : # negative sign here is important , cause we compare +ve with -ve otherwise 
                heapq.heapreplace(heap , (-distance , x , y))
            
        
        return [[x,y] for _, x , y in heap]








        