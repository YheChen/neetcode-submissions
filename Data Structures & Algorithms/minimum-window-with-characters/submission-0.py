from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        window = Counter()

        have = 0
        need_types = len(need)

        left = 0
        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_types:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]