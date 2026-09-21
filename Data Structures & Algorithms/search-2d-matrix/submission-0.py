class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # eg : Input: matrix = [[1,2,4,8],[10,11,12,13]]
        # rows = len(matrix) = 2 
        # columns = len(matrix[0]) = 4 


        rows = len(matrix)

        columns = len(matrix[0])

        #left is 1st value and right is last value 
        left = 0
        right = rows * columns - 1 # in our eg : matrix[left] = 1 and matrix[right] = 13

        while left <= right :
            # " // " is floor division 
            middle = (left + right) // 2  # 3 in our eg 

            row = middle // columns # 0 in our eg 

            column = middle % columns # 3 in our case 

            value = matrix[row][column]

            if value == target :
                return True 
            
            elif value < target :
                left = middle + 1
            
            else :
                right = middle - 1
            
        return False



