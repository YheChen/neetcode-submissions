class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        output = []

        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return
            for i in range(col):
                r += dr
                c += dc
                output.append(matrix[r][c])
            dfs(col, row - 1, r, c, dc, -dr)
        dfs(rows, cols, 0, -1, 0, 1)
        return output