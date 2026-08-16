class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        num_islands = 0
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or (r, c) in seen or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            seen.add((r, c))
            for direction in DIRECTIONS:
                dfs(r + direction[0], c + direction[1])
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)
        return num_islands