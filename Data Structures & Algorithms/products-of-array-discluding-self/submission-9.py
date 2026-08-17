class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1] * n
        pref_prod = [-1] * n
        suff_prod = [-1] * n
        pref_prod[0] = nums[0]
        for i in range(1, n):
            pref_prod[i] = nums[i] * pref_prod[i - 1]
        suff_prod[-1] = nums[-1]
        # for i in range(2, n - 1):
        #     suff_prod[-i] = nums[-i] * suff_prod[1 - i]
        for i in range(1, n):
            suff_prod[n - 1 - i] = nums[n - 1 - i] * suff_prod[n - i]    
        output[0] = suff_prod[1]
        output[n - 1] = pref_prod[n - 2]
        for i in range(1, n -1):
            output[i] = pref_prod[i - 1] * suff_prod[i + 1]
        return output