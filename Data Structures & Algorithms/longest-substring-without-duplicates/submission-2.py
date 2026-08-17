class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substr = defaultdict(int)
        l = 0
        for r in range(len(s)):
            substr[s[r]] += 1
            while substr[s[r]] > 1:
                substr[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest