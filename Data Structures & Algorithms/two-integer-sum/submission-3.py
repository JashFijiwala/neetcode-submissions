class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums[0:i] or rem in nums[i+1:]:
                result.append(i)
                j = i + 1
                while(True):
                    if nums[j] == rem:
                        result.append(j)
                        return result
                    j += 1
                    
            