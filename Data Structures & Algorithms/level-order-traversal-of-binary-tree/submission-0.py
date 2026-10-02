# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None :
            return []

        #we will start by creating empty list called queue , level , result 
        result = [] 

        #queue contains all elements in that level only 
        queue = deque([root])

        while queue :
            level = []

            #size of level is the no of elements in that level = size of queue 
            level_size = len(queue)


            #iterate the queue 
            for _ in range(level_size) :

                # add all vales into the level list
                node = queue.popleft() #popleft removes val from front 
                level.append(node.val)

                if node.left :
                    
                    # add that to the queue 
                    queue.append(node.left)
                
                if node.right :
                    queue.append(node.right)
            
            
            # add every level once done onto the result 
            result.append(level)
        
        return result 






        