class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # We need to check if box is valid in current form 
        # we will create 3 sets to check if number is in row , column or box

        #1. Create 3 sets 
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] # 9 boxed of 3 x 3 

        #2. visit all these cells to check what number is present 
        for row in range(9) :
            for column in range(9) :
                number = board[row][column] 

        
        # 3. check if number is present or not 
                if number == "." :
                    continue

                box_index = (row // 3) * 3 + (column // 3)
        #.4. if number is there check duplicates 

                if (number in rows[row] or 
                    number in columns[column] or 
                    number in boxes[box_index]
                    ):
                    return False
            
        # 5. else add number to that index 

                rows[row].add(number)
                columns[column].add(number)
                boxes[box_index].add(number)

    
        return True



        
        