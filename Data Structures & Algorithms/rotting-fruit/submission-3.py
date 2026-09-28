from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        fresh_oranges = 0
        minutes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        print(q, fresh_oranges)
        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = row + dr, col + dc
                    if nr >= rows or nc >= cols or nr < 0 or nc < 0:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh_oranges == 0 else -1
