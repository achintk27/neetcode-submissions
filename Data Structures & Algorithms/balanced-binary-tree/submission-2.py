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

        #helper function to return the depth and wether the tree is balaced 
        def check(node) :

            if node is None :
                return True , 0 # true for balanced , 0 for depth 
            
            left_balanced , left_depth = check(node.left)
            right_balanced , right_depth = check(node.right)

            #its considered balanced only if left is balanced , right is balanced and the diff in depth <= 1
            balanced = (left_balanced and right_balanced and abs(left_depth - right_depth) <= 1 )

            depth = 1+ max(left_depth , right_depth)
            return balanced , depth 
        
        balanced, depth = check(root)
        return balanced




