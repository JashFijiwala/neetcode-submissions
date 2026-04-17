class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        postfix = 1

        for i in range(length-1):
            result[i+1] *= nums[i] * result[i]

        for i in range(length-1, 0, -1):
            postfix *= nums[i]
            result[i-1] *= postfix

        return result