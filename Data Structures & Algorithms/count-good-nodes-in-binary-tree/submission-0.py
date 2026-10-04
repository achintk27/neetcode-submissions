# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # we use dfs approch 
        def dfs(node , laragest_so_far) :
            if node is None :
                return 0 

            #if the values of node is greater than the largest value so far 
            good = 1 if node.val >= laragest_so_far else 0 

            new_largest = max(laragest_so_far ,node.val)

            #we need count on left and right 
            left_count = dfs(node.left , new_largest)
            right_count = dfs(node.right , new_largest)

            return good + left_count + right_count
        
        return dfs(root , root.val)




        








        


























        





        

        


        
