class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # we compare lem of t and s such that if t > s , s cant have all elements of t (casue include deplicates)
        if not t or len(t) > len(s) :
            return ""
        
        #we create a dictonary needed to store the char and its count in t 
        needed = {}

        #iterate through t and add its char and count into needed 
        for char in t :
            needed[char] = needed.get(char , 0) + 1 

        
        #create few variables : 

        #window is a dictonary used to move and find the substring 
        window = {}

        #required is how many char types we need to get the substring
        required = len(needed)

        #have is how many of the char in needed do we have 
        have = 0 

        #left is a pointer to start iteration 
        left = 0 

        best_length = float("inf")
        
        #to find the best start position of substring 
        best_start = 0

        #iterate through s 
        for right in range(len(s)) :
            char = s[right]
            window[char] = window.get(char , 0) + 1


            #if all char and there and window == needed 
            if char in needed and window[char] == needed[char] :
                have += 1
            

            #once we have all the elements , shorten the window 
            while have == required :

                #length of window 
                length = right - left + 1 

                if length < best_length :
                    best_length = length  
                    best_start = left
                
                #if not we need to shorten the window 
                leaving = s[left]
                window[leaving] -= 1 

                #check if removing a char made the substring incomplete 
                if leaving in needed and window[leaving] < needed[leaving] :
                    have -= 1
                

                left +=1 
            
        if best_length == float("inf"):
            return ""
        

        return s[best_start:best_start + best_length]


        


        

        