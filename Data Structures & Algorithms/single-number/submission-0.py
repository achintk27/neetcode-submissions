class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #use XOR operation 
        # 0 ^ 0 = 0 
        # 0 ^ 1 = 1 
        # 1 ^ 0 = 1 
        # 1 ^ 1 = 0 

        #it gives the value when the bits differ 
        # a ^ 0 = a , a ^ a = 0 

        # 3 = [ 0 , 1 , 1 ] , 2 = [0 , 1 , 0] , apply XOR to all columns = [0 , 0 , 1] = 1
        # next 1 ^ 3 = [0 , 1 , 0] = 2 , this is the result 

        result = 0 

        for num in nums : 

            result = result ^ num
        
        return result 


        