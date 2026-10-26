class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 4 = [0 1 0 0]
        # 7 = [0 1 1 1]
        # 11 =[1 0 1 1]

        #4 ^ 7 = [0 0 1 1]
        # AND tells us where the carry is , 4 & 7 = [0 1 0 0] , carry was the pos 2
        # now the carry value should be added to the left element so , perform << 1

        #so at each bit we need to check carry 

        MASK = 0xFFFFFFFF      # 32 ones
        MAX_INT = 0x7FFFFFFF   # Largest signed 32-bit positive integer

        while b != 0 :

            #calculate the carry 
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry
        
        if a <= MAX_INT :
            return a
        
        return ~(a ^ MASK)
        



