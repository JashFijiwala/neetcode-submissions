class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for value in nums:
            if value in check:
                return True
            else:
                check.add(value)
        return False