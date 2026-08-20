class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is rows, n is cols
        rows, cols = m, n
        dp = [[-1] * n for _ in range(m)]
        for r in range(rows):
            dp[r][0] = 1
        for c in range(cols):
            dp[0][c] = 1
        
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]