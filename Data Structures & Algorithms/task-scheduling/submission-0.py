class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #count how many times each iteam appears
        counts = Counter(tasks)

        #create a max heap having count of all elements , so essentially if an element has to be executed 4 times , heap stores 4 
        heap = list(counts.values())
        
        #create a max heap
        heapq.heapify_max(heap)

        #use a queue that would store the amount of time we need to wait to execute the repeated task
        cooldown = deque()
        time = 0 

        #while a task is present in the heap , add time 
        while heap or cooldown:
            time += 1 
        
        
            #every task is available to be executed when its cooldown ends 
            while cooldown and cooldown[0][1] <= time : 
                
                #for each waiting task we store 2 things : 
                # remaning is no of times it still needs to be executed , ready_time is when the task is allowed to run again 
                remaining, ready_time = cooldown.popleft() 

                heapq.heappush_max(heap, remaining)


            #execute task at root (i.e the one with most occurances left)
            if heap : 
                remaining = heapq.heappop_max(heap)
                remaining -= 1 
            
            #if there are most instances of this task add it to the queue 
                if remaining > 0 :
                    cooldown.append((remaining , time + n + 1 ))
    
        return time







        