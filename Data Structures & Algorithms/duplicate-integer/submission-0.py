class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for k in range(len(nums) - 1):
            if nums[k] == nums[k + 1]:
                return True
        return False
