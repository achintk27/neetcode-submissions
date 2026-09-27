class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        longest = 0 

        #iterate through the string 
        for right in range(len(s)) :

            #check if right is in seen , if repeating
            while s[right] in seen :

                #remove all the seen values 
                seen.remove(s[left]) 
                left += 1 
            
            #if the char is not in seen 
            seen.add(s[right])


            count = right - left + 1
            longest = max(longest , count )
        
        return longest 



        