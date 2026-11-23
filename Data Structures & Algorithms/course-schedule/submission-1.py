class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #intution : we can draw a graph , we can reach course 1 only from course 0 , it will be a directed graph. start with coures that need to prerequisite. others will become available. if there is any closed loop that we cant enter then return False. else true 

        #create an empty array of size equal to the number of courses which stores which courses depend on a given course
        next_courses = [[] for _ in range(numCourses)] 


        #also create an array remaning which will store how many more prereq are needed to unlock a course. 
        remaining = [0] * numCourses


        # add all the courses from prerequisites array into nextcourse and increment the remaining 
        for course , prerequisite in prerequisites : 
            
            # course b needs course a to be finished first. once course a is complete course b becomes unlocked 
            next_courses[prerequisite].append(course)

            #record how mant preq course course b need to be unlocked
            remaining[course] += 1


        #create a queue that will take all the course that have no remaining prereq 
        queue = deque()
            

        for course in range(numCourses) :
            if remaining[course] == 0 :
                queue.append(course)

            
        completed = 0


        #while elements are there in the queue we check if all the courses are completed
        while queue : 

            course = queue.popleft()
            completed += 1 


            #as we pop elements form the queue the pre reqs are also continously lowering 
            for next_course in next_courses[course] :
                remaining[next_course] -= 1 

                #if the pre req = 0 , add the course to the queue
                if remaining[next_course] == 0 :
                    queue.append(next_course)
            

        #true if all are completed 
        return completed == numCourses



















        