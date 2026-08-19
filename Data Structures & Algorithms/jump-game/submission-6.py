class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = nums[0]
        for i in range(1, len(nums)):
            if fuel <= 0:
                return False
            fuel = max(fuel - 1, nums[i])
        return True