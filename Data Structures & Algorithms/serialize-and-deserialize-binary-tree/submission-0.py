# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#serialise : comvert binary tree into string 
#deserialise : convert string back into binary tree 

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        #create an empty list parts that stores all the numbers as a string 
        parts = []

        def dfs(node) :

            #store NULL as #
            if node is None : 
                parts.append("#")
                return
            
            #store if its a value 
            parts.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        #return comma seperated values 
        return ",".join(parts)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        #find the value based on comma 
        parts = data.split(",")
        index = 0 

        def dfs() :

            nonlocal index

            #value of node will be the value at a perticular index 
            value = parts[index]
            index += 1

            #empty node will have # in the list 
            if value  == "#" :
                return None 
            
            node = TreeNode(int(value))
            node.left = dfs()
            node.right = dfs()
            return node
    
        return dfs()
















