class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x in seen:
                return [i, seen[x] - 1]
            seen[nums[i]] = i + 1


