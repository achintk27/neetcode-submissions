# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #we use two main variables : 
        # 1. Lower : the lowest value a node can have. , so for 1st node thats -infinite 
        # 2. upeer : the max valu a node can have , for 1st node , its infinite

        def check (node , lower , upper) :
            if node is None :
                return True 

                #the node value should always be greater than lower and less than upper 
            if not(lower < node.val < upper) :
                    return False

            return (
                #max value a child node on left can have is parent value , min is -infinite 
                check(node.left , lower , node.val) 

                #lowest value a right child can have is the parent value , max is - infinite 
                and check(node.right , node.val , upper)
            )

        return check(root , float("-inf"), float("inf"))
                








        