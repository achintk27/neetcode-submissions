class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        #very similar to course schedule 1

        #create an array that has what course needs what pre req 
        next_courses = [[] for _ in range(numCourses)]

        #create an array remaining that tells us many more pre req are needed for a course to be eligible to be taken
        remaining = [0] * numCourses


        # for all the values in the given array , store what course needs what prereq and add in to the next_courses array. We also increment the remaining 
        for course , prerequsite in prerequisites : 
            
            # we add the course that can be taken once pre req is done. so if b must be completed to take a , in the index val of b at the next_courses array we add a. 
            next_courses[prerequsite].append(course)
            remaining[course] += 1 
            

        queue = deque()

        #iterate through all the coursed and once all pre req have been completed for a course add that course into the queue
        for course in range(numCourses) :
            if remaining[course] == 0 :
                queue.append(course)
        

        #create a new array order to return the order of completion at the end 
        order = []


        # while we have elements in the queue , we pop them from the left and add it into the order array.
        while queue : 
           course = queue.popleft()
           order.append(course)

           
           #next_course cantains all the pre req needs for a course  , so are we unlock more courses , we can start looking into this array to find new unlocked courses. 
           for next_course in next_courses[course] :
                remaining[next_course] -= 1 

                if remaining[next_course] == 0 :
                    queue.append(next_course)
            

        if len(order) == numCourses :
            return order 

        
        #if we cant unlock all courses , return empty array 
        return []














        