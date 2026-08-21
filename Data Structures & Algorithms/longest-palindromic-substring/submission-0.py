class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        best_start, best_len = 0, 1

        for i in range(n):
            dp[i][i] = True
        
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if s[l] == s[r]:
                    if length == 2 or dp[l + 1][r - 1]:

                        dp[l][r] = True

                        if length > best_len:

                            best_start = l

                            best_len = length
        return s[best_start:best_start + best_len]