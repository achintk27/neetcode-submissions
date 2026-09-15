class Solution:

    def encode(self, strs: List[str]) -> str:
        # we are going to solve this by getting : 
        # "char count" + " # " + "word"
        # so ["Hello", "World"] = [5#hello5#world]

        parts = []

        for word in strs :
            parts.append(str(len(word)) + "#" + word)
        
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        # we will decode in 5 steps 
        # 1. find #
        # 2. look at the number before that 
        # 3. take those many chars from there 
        # 4. move to next length 

        result = []
        i = 0 

        while i < len(s) :
            j = i 
            while s[j] != "#" :
                j = j + 1
            
            length = int(s[i:j]) # includes i , exludes j. So here if its ["5#hello"] , i = 0 = "5" , j = 1 = #. therefore length = 5 
            start = j + 1
            end = start + length # here end = 2 + 5 = 7 

            result.append(s[start:end]) # appends ["hello"]
            i = end 

        return result 
