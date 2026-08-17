from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freqs = Counter(t)
        freqs = defaultdict(int)

        need = len(t_freqs)
        have = 0

        shortest = ""
        l = 0

        for r in range(len(s)):
            c = s[r]
            freqs[c] += 1

            # This character just reached the required frequency
            if c in t_freqs and freqs[c] == t_freqs[c]:
                have += 1

            # Window is valid
            while have == need:
                # Update answer
                if not shortest or r - l + 1 < len(shortest):
                    shortest = s[l:r + 1]

                # Remove left character
                c = s[l]
                freqs[c] -= 1

                # We just dropped below the required frequency
                if c in t_freqs and freqs[c] < t_freqs[c]:
                    have -= 1

                l += 1

        return shortest