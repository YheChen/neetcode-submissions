class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_freq = 0
        freqs = defaultdict(int)
        l = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            max_freq = max(max_freq, freqs[s[r]])

            while (r - l + 1) - max_freq > k:
                freqs[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        return longest