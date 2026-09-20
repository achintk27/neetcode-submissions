class Solution:
    def isPalindrome(self, s: str) -> bool:

        #We need 2 pointers , one points to the start and one to the end.
        #until left < right , check if s[left] == s[right]

        left = 0 
        right = len(s) - 1

        #check when left < right 
        while left < right :

            # we need to skip non letter and non number char 
            while left < right and not s[left].isalnum() :
                left += 1 

            while right > left and not s[right].isalnum() :
                right -= 1
            
            #check if they are the same 
            if s[left].lower() != s[right].lower() :
                return False 
            
            left += 1
            right -= 1
            
        return True   



        