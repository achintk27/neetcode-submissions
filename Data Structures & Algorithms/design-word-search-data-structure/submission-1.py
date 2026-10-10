class TrieNode :

    def __init__(self) :

        #create a dictonary to store char as key , node as value 
        self.children = {}

        #check if its the end of the word 
        self.is_end = False 


class WordDictionary:

    def __init__(self):
        
        #create new node 
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        
        current = self.root 

        #same as insert a word 
        for char in word :

            #check if its there in children 
            if char not in current.children :

                #create the node , if not present 
                current.children[char] = TrieNode()
            
            #if present , move current there 
            current = current.children[char]
        
        current.is_end = True 
        

    def search(self, word: str) -> bool:

        #use DFS
        def dfs(index , node ) :

            #here we see , starting as this trie node , can i match the rest of the node. 
            
            #when we match all the chars and reach the last node , we need to return is_end 
            if index == len(word) :
                return node.is_end 
            
            #if its not , then move the char 
            char = word[index]
            
            #if the node is " . " it can be any char , so iterate through the values of children 
            if char == "." :

                for child in node.children.values() :
                    
                    #the dot can have multiple values , so we check 
                    if dfs(index + 1 , child) :
                        return True 
                    
                return False 

            #a char must have exact match 
            if char not in node.children :
                return False 
            
            return dfs(index + 1 , node.children[char])
        
        return dfs(0 , self.root)

            






        
