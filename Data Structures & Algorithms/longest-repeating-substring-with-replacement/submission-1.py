class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #create a directory to store count of each char as key value pairs 
        counts = { }
        left = 0
        longest = 0 

        #iterate through the string 
        for right in range(len(s)) :

            # lets assign a variable : char to each char we iterate through 
            char = s[right]
            counts[char] = counts.get(char , 0) + 1 


            #check if number of changes needed > k 
            while (right - left + 1 ) - max(counts.values()) > k :

                #if its > k , the count of max char decreases , we move to next number 
                counts[s[left]] -= 1 
                left +=1 

            #if changes <= k 
            longest = max(longest , right - left + 1)
        
        return longest 
        

        