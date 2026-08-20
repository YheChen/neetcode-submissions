class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        top_row = False
        left_col = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # set start of row to 0
                    if r == 0:
                        top_row = True
                    else:
                        matrix[r][0] = 0
                    # set start of col to 0
                    if c == 0:
                        left_col = True
                    else:
                        matrix[0][c] = 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0

        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0
        if top_row:
            for c in range(cols):
                matrix[0][c] = 0
        
        if left_col:
            for r in range(rows):
                matrix[r][0] = 0

        