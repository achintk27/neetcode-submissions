# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #number of edges passing through that node is diameter 
        diameter = 0

        #create a helper function that is used to caliculate max depth of every node 
        def depth(node) :
            nonlocal diameter #this says change diameter every time when depth changes 

            #caliculate max depth 
            if node is None :
                return 0 
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            #longest path that goes through this node 
            diameter = max(diameter , (left_depth + right_depth))

            #the number of nodes that a perticular node reports to its parent
            return 1+ max(left_depth , right_depth)
        
        depth(root)
        return diameter 


        