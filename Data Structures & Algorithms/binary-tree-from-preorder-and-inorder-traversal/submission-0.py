# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        #preorder : root , left , right 
        #inorder : left , root ,right 

        #pre order will give us the root of the tree 
        #inorder tells us what is the left and right 

        # Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
        #from this we know root is 1 , find 1 in inorder and all elements on either side of 1 are left and right 
        #continue recursion of this 


        #use hashmap to store index of valus 
        index = {val : i for i , val in enumerate(inorder)}
        
        #use this to traverse preorder 
        self.pre_indx = 0 

        #create a window that needs to be considered when building subtree
        def build(left , right):
            
            #no values left
            if left > right :
                return None 

            root_val = preorder[self.pre_indx]
            self.pre_indx += 1
            root = TreeNode(root_val)

            #now we need left and right 
            mid = index[root_val]

            root.left = build(left , mid - 1)
            root.right = build(mid + 1 , right)
            return root
        
        #consider entire inorder array first 
        return build(0 , len(inorder) - 1)





    




        