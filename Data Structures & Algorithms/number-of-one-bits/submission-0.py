class Solution:
    def hammingWeight(self, n: int) -> int:

        
        #we use AND operation and compare with 1 

        #23 = [1,1,1,1] = 1111
        #perform 1111 and 1 next right shift and perform 111 & 1 , next 11 & 1 
        
        #AND
        # 1 & 1 = 1 
        # 0 & 1 = 0
        # 0 & 1 = 0 
        # 0 & 0 = 0 

        count = 0 

        while n > 0 :
            count += n & 1 

            n = n >> 1 
        
        return count 



        
        