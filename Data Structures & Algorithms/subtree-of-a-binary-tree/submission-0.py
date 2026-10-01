# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #does any node in root begin a tree that contains same as subroot 
        
        #if there is no subroot , then return true 
        if subRoot is None :
            return True 
        
        #if there is no root , then false 
        if root is None :
            return False 
        
        #we check 2 things. 
        #1. Is there a node in root same as that in subtree 
        #2. Are nodes connecting to the node the same as that of subtree 

        # Check if bith tress are same / subroot is in root
        if self.isSametree(root , subRoot) :
            return True 

        #if both the roots are different , we check the children 
        return (self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot))
    
    #Once we found the matching root , check if children and other nodes connecting are same
    def isSametree(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:

        #if the subroot and root has no chilren 
        if first is None and second is None :
            return True 
        
        #if only one is none 
        if first is None or second is None :
            return False

        #check f values match 
        if first.val != second.val :
            return False 
        
        #return True if both left and right val are same 
        return (self.isSametree(first.left , second.left) and self.isSametree(first.right , second.right))








