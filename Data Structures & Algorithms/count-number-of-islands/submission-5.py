class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == '0':
                return
            visited.add((r, c))

            for dx, dy in DIRS:
                dfs(r + dx, c + dy)
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands



