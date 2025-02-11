class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        prefix = 0
        count = defaultdict(int)
        count[0] = 1

        for x in nums:
            prefix += x
            if count[prefix - k] >= 1:
                res += count[prefix - k]
            count[prefix] += 1

        return res
