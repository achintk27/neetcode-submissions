class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        #very similar to valid graph tree , so here we start from a node , perform DFS and visit all nodes possible from there. if there is an unvisited node it must start a new component. we use stack for DFS again. 
        neighbours = [[] for _ in range(n)] 


        #every edge has 2 values , it specifies which two values does the edge connect
        for a , b in edges :

            # add them to neighbours array 
            neighbours[a].append(b)
            neighbours[b].append(a)
        

        visited = set()
        components = 0


        #use a start node and iterate
        for start in range(n) :

            #if we have already visited it , continue. if not we increae the components 
            if start in visited :
                continue
            
            components += 1 
            
            #start is the first node of stack to begin , start is node number 
            stack = [start]


            #visit all the nodes that are in the stack. this will be all nodes of 1 component
            while stack : 
                node = stack.pop()


                #if we have vivited that node , continue , else add to the set 
                if node in visited : 
                    continue 
                
                visited.add(node)


                # for each node add all its neighbours onto the stack , these are all the node we are yet to visit 
                for neighbour in neighbours[node] :
                    if neighbour not in visited : 
                        stack.append(neighbour)
            
        return components

        
