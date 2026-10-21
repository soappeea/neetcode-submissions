class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # mult or equal is same regardless since 1 * prefix = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # must multiply since apply postfix to result
            postfix *= nums[i]
        return res