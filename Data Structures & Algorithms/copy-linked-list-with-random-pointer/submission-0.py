"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # node.next --> next 
        # node.random ---> any node or None 

        # checking if anything is there in the list 
        if not head :
            return None 

        # create a dictonary 
        old_to_new = { }

        #Create a new new for every old node 
        current = head 

        while current :
            #creates a new node for all old nodes 
            old_to_new[current] = Node(current.val)
            current = current.next 


        # Now we need to connect the nodes to other nodes
        current = head 

        while current :

            #use a variable copy that refers to new node corresponding to current Node 
            copy = old_to_new[current]

            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)

            current = current.next 
        
        return old_to_new[head]










        