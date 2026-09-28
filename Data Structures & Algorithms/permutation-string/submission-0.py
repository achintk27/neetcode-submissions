class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #every element of s1 has to be present in s2 , hence if len(s1) > s2 then false
        if len(s1) > len(s2) :
            return False 
        
        #create a dictonary needed , that stores the char in s1 and their count , so we look for those many of each char in s2
        needed = {}

        #create a dictonary to slide the window in s2 to find the same char
        window = {}

        #iterate through s1 and store the chars and count in needed 
        for char in s1 :
            needed[char] = needed.get(char , 0) + 1 
        
        #Build window for s2 
        for i in range(len(s1)) : # we need window as len of s1 
            char = s2[i]
            window[char] = window.get(char , 0) + 1

        #if needed = window - true 
        if window == needed :
            return True 
        
        #loop through indexes starting from len(s1) and stop before length(s2)
        for right in range(len(s1), len(s2)) : # starts from last index of s1 

            #lets assign 2 variables to move the window 
            entering = s2[right] 
            leaving = s2[right-len(s1)]

            window[entering] = window.get(entering , 0) + 1 

            #move the window to the left 
            window[leaving] -= 1 

            #if window of leaving = 0 , no more char 
            if window[leaving] == 0 :
                del window[leaving]
            

            if window == needed :
                return True 
        
        return False 
            








