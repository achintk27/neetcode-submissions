class Solution:
    def countBits(self, n: int) -> List[int]:

        #Number of 1's in i = count of 1's in (i >> 1) + (i & 1)
        
        #create a list having n + 1 zeros
        answer = [0] * (n + 1)

        for i in range(1 , n+1) :
            answer[i] = answer[i >> 1] + (i & 1)
        
        return answer