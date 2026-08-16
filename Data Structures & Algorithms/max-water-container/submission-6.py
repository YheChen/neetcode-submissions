class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l, r = 0, len(heights) - 1

        def areaHelper(l, r) -> int:
            return min(heights[l], heights[r]) * (r - l)
        
        while l < r:
            most = max(areaHelper(l, r), most)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return most