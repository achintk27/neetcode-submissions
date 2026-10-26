class Solution:
    def reverseBits(self, n: int) -> int:

        #initially all are 0
        result = 0 

        for _ in range(32) :
            
            #shift result left by 1 , take the rightmost bit from n , perform "&" with 1 , OR it into the result 
            result = (result << 1) | (n & 1)
            n = n >> 1
        
        return result



        