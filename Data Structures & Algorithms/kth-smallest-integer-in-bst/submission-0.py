# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #we use stack and tree 
        stack = []

        #traverse the tree 
        current = root

        while current or stack :
            
            #traverse the left part
            while current :
                stack.append(current)
                current = current.left

            #next smallest node 
            current = stack.pop()
            k -= 1 

            #when k == 0 we have found the smallest element 
            if k == 0 :
                return current.val
            
            #if not , check the right
            current = current.right



        