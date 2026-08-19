class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        res = 0
        for num in nums:
            res ^= num
        for i in range(0, n):
            res ^= i
        return res