class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #valid tree : No cycle 
        #if a graph has n nodes , a tree must have n -1 edges
        

        #first check based on number of edges 
        if len(edges) != n - 1 :
            return False 

        
        #build an undirected graph
        
        #neighbours store the neighbur of that index value in that position. each index could have more than 1 value 
        neighbours =  [[] for _ in range(n)] 

        #each edge has 2 values which tell us which two nodes are connected through that edge
        for a , b in edges :
                
            #a will be neighbour of b and vice versa. store this in the array
            neighbours[a].append(b)
            neighbours[b].append(a)

            
        #visit every node in the array from node 0 and add to a set. We use set cause order doesnt matter 
        visited = set()
            
        #we add all the elements to a stack that we are yet to explore 
        stack = [0]

        #while we have elements in the stack (unvisited nodes) , pop them. 
        while stack :
            node = stack.pop()

            #as we look at all the elements popped from the stack , check if we have visted there beofre 
            if node in visited : 
                continue 
                
            #if its a new element we havent visited before add it to visited
            visited.add(node)


            for neighbour in neighbours[node] :
                if neighbour not in visited :
                    stack.append(neighbour)
            
            
        return len(visited) == n







