class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if s[l] == s[r]:
                    if length == 2 or dp[l + 1][r - 1]:
                        dp[l][r] = True
                        count += 1
        return count 