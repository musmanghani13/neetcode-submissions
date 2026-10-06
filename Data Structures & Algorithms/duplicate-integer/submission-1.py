class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        if len(set(nums)) < len(nums):
            return True
        return False

