# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        #best is initially going to be -infinite 

        best = float("-inf")

        #we use dfs 
        def dfs(node) :
            
            #best changes based on the output
            nonlocal best 

            if node is None :
                return 0 
            
            
            #if the sum makes it less than current sum or best , ignore 
            left_gain = max(0 , dfs(node.left))
            right_gain = max(0 , dfs(node.right))

            #a complete path means we add both sides \
            path_through_node = left_gain + node.val + right_gain
            best = max(best ,path_through_node)

            #check with path , left or right should we extend it to
            return node.val + max(left_gain , right_gain)
        
        dfs(root)
        return best



        