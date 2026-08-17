from collections import Counter
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freqs = Counter(t)
        freqs = defaultdict(int)
        shortest = ""
        l = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            if all([t_freqs[x] <= freqs[x] for x in t_freqs]):
                while freqs[s[l]] > t_freqs[s[l]]:
                    freqs[s[l]] -= 1
                    l += 1
                if not shortest or r - l + 1 < len(shortest):
                    shortest = s[l:r + 1]
        return shortest