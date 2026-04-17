class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        for i in range(length-1):
            result[i+1] *= result[i] * nums[i]

        postfix = 1

        for i in range(length-1, 0, -1):
            postfix *= nums[i]
            result[i-1] *= postfix


        return result
