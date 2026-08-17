class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # left sorted
                if nums[l] <= target <= nums[mid]: # target here
                    r = mid
                else: # target not here
                    l = mid + 1
            else: # right sorted
                if nums[mid] < target <= nums[r]: # target here
                    l = mid + 1
                else: # target not here
                    r = mid
            
        return -1
