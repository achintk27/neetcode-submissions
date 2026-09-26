class Node :
    def __init__ (self , key = 0 , value = 0 ) :
        self.key = key
        self.value = value 
        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        #create an empty dictonary to store cache 
        self.cache = { }

        #we use doubly linked list 
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.previous = self.left


    #left most is oldest and right most is newest
    def remove(self, node) :
        before = node.previous 
        after = node.next 

        before.next = after 
        after.previous = before
    
    def insert(self , node) :
        before = self.right.previous
       
        before.next = node
        node.previous = before
        node.next = self.right
        self.right.previous = node



    def get(self, key: int) -> int:

        #check if key is not present 
        if key not in self.cache :
            return -1 

        #if key is present 
        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:

        if key in self.cache :
            node = self.cache[key]
            node.value = value 
            self.remove(node)
            self.insert(node)
        
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.insert(node)


        if len(self.cache) > (self.capacity) :
            #deletes the 1st element in LL
            oldest = self.left.next
            self.remove(oldest)
            del self.cache[oldest.key]





        
