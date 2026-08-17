class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        most = 0
        l, r = 0, n - 1
        while l < r:
            if heights[l] < heights[r]:
                water = heights[l] * (r - l)
                l += 1
            else:
                water = heights[r] * (r - l)
                r -= 1
            most = max(most, water)
        return most