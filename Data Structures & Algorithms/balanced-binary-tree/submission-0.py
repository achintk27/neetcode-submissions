# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None :
            return True 
        
        def depth(node) :

            if node is None :
                return True 

            left_depth = depth(node.left)
            right_depth = depth(node.right )

            return 1 + max(left_depth ,right_depth)
        
        left_depth = depth(root.left)
        right_depth = depth(root.right)
            
        if abs(left_depth - right_depth) > 1 :
            return False 
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        