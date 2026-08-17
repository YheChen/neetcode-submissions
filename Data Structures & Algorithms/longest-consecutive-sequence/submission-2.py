class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        seen = set()
        longest = 0
        for num in nums:
            if num in seen:
                continue
            start = num
            seen.add(num)
            curr = 1
            while num + 1 in nums:
                curr += 1
                seen.add(num + 1)
                num += 1
            longest = max(longest, curr)
        return longest