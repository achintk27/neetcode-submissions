#Building a trie makes it easier to find words due to same prefix 

class TrieNode :
    def __init__(self) :

        #"children" dictonary will have key as the char and value as the node 
        self.children = {}
        
        #store the full word if the word ends here : 
        self.word = None 

    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        #build a trie 
        root = TrieNode()

        #iterate through the words 
        for w in words :

            node = root

            #check if the char in the word is present in children 
            for ch in w :

                if ch not in node.children :

                    # add the word 
                    node.children[ch] = TrieNode()
                
                #if word is present , move the node to that char 
                node = node.children[ch] 
            
            #at the last node of the word , store the entire word 
            node.word = w 



        #define the rows and columns of the board 
        rows , columns = len(board) , len(board[0])
        result = []

        #we do dfs 
        def dfs(r , c , parent) :

            #the char on the board :
            ch = board[r][c]

            #move the node to the child node from parent , so move the node one level down in the tree
            node = parent.children[ch]


            #if the node has a word , append result 
            if node.word :
                result.append(node.word)

                #since we cant use it again 
                node.word = None 
            
            #marks the point as visited 
            board[r][c] = "#"


            #check the 4 neighbours , down ( 1, 0 ) , left (0 , -1) , right(0 , 1) , up (- 1, 0) , dr = dicrection row 
            for dr , dc in ((1 , 0) , (-1 , 0) , (0 , -1), (0 , 1)) :

                #new row (nr) = r + dr , new column(nc) = c + dc
                nr , nc = r + dr , c + dc

                #check 3 conditions : 
                #1. nr must be inside the board
                #2. new column must be inside the board
                #3. the neighbour must letter continues some word in the trie 

                if (0 <= nr < rows and 0<= nc < columns and board[nr][nc] in node.children) :

                    #continue dfs , pass node as new parent 
                    dfs(nr , nc , node)
                
            #once done move back to the ch , that we put # as a different path might need this cell 
            board[r][c] = ch 


            #if a node has no children left and no words ending here , delete it 
            if not node.children and node.word is None :
                del parent.children[ch]
            

        #call dfs for all cells in board 

        for r in range(rows) :
            for c in range(columns) :

                if board[r][c] in root.children :
                    dfs(r , c , root)
        
        return result 




        

        