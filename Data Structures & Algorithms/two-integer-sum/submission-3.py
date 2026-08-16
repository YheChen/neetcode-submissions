class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in complement:
                return [complement[target - nums[i]], i]
            complement[nums[i]] = i
        