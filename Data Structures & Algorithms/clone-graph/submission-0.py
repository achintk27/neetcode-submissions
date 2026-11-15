"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #the entire graph is connected and undirected
        #we have the values and all neighbours of a node
        #we can use a hash map  , to map old node to new node , so old 1 --- new 1 

        if node is None : 
            return None 

        # we use hash map to store the clones 
        clones = {}


        #perform DFS operation using original value to find and connect all nodes 
        def dfs(original) :

            #first check if the node is already cloned , if it is just return the value 
            if original in clones : 
                return clones[original] # if original = A , it return A' which is the cloned value

            
            #else create the clone , it has same value as original. 
            copy = Node(original.val)
            clones[original] = copy 


            #connect the neighbours of the clones
            for neighbor in original.neighbors :
                copy.neighbors.append(dfs(neighbor))


            return copy 

        return dfs(node)





