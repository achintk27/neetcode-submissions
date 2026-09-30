# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #very simple , just swap left and right child of all nodes 
        #We use recursion 

        if root is None :
            return None 

        root.left , root.right = root.right , root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
    
        return root
        


        