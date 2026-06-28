class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if not d.get(n):
                d[n] = True
            else:
                return True
        return False
