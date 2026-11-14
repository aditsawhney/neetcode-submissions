class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, (rows*cols-1)

        while left <= right:
            mid = (left+right)//2
            
            curr_row = mid//cols
            curr_col = mid%cols
            
            if matrix[curr_row][curr_col] == target:
                return True
            elif matrix[curr_row][curr_col] > target:
                right = mid-1
            else:
                left = mid+1
        
        return False
