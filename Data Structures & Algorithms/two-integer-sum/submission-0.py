class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k, n in enumerate(nums):
            if d.get(n) is not None:
                return [d[n], k]
            d[target - n] = k
        return []
