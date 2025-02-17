class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        right, left = 0, 0
        pairs = 0
        mp = defaultdict(int)

        for right in range(n):
            mp[nums[right]] += 1
            pairs += mp[nums[right]] - 1

            while pairs >= k:
                res += n - right
                pairs -= mp[nums[left]] - 1
                mp[nums[left]] -= 1
                left += 1

        return res

