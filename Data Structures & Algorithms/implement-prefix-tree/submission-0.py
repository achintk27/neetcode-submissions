#stores the string by breaking it into individual chars and store based on common prefixes 
#eg : if we have to store "app" and "apple" 
#root ---> a ---> p ---> p ---> l ---> e
                    #app ends here      #apple ends here 


class TrieNode:

    def __init__(self):

        #create a dictonary "children" that contains charecter as key and clid node is value 
        self.children = {}

        #we need to check if the word ends here : 
        self.is_end = False 

class PrefixTree :

    def __init__(self):

        #crete the node 
        self.root = TrieNode()


    def insert(self, word: str) -> None:

        #iterate using curent 
        current = self.root

        #first check if the char is there in the children dictonary 
        for char in word : 

            #if char is not presnt :
            if char not in current.children :

                #create node and insert the value 
                current.children[char] = TrieNode()

            #if char is present , current moves to that char 
            current = current.children[char]
        
        #when word is done change the is_end to true
        current.is_end = True 


    def search(self, word: str) -> bool:

        #again iterate from root 
        current = self.root 

        #check if present 
        for char in word :

            #if not present , retuen false 
            if char not in current.children :
                return False 
            

            #if presnt , move current to the node and return true
            current = current.children[char]

        return current.is_end 

        

    def startsWith(self, prefix: str) -> bool:

        #again iterate from root 
        current = self.root 

        #iterate and check 
        for char in prefix :

            #check with children 
            if char not in current.children :
                return False 
            
            current = current.children[char]
        
        return True


        









        