class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check for rows
        for i in range(9):
            row_set = set()
            for j in range(9):
                value = board[i][j]
                if value == ".":     # skip for empty values
                    continue
                elif value in row_set:
                    return False
                else:
                    row_set.add(value)
        
        # check for columns
        for j in range(9):
            col_set = set()
            for i in range(9):
                value = board[i][j]
                if value == ".":    # skip empty values
                    continue
                elif value in col_set:
                    return False
                else:
                    col_set.add(value)
        
        # check for boxes
        row_start, row_end = 0, 2
        col_start, col_end = 0, 2

        while row_end < len(board):
            box_set = set()
            for i in range(row_start, row_end + 1):
                for j in range(col_start, col_end + 1):
                    value = board[i][j]
                    if value == ".":    # skip empty values
                        continue
                    elif value in box_set:
                        return False
                    else:
                        box_set.add(value)
            
            col_start += 3
            col_end += 3

            if col_start >= len(board[0]):
                col_start, col_end = 0, 2
                row_start += 3
                row_end += 3
        
        return True



