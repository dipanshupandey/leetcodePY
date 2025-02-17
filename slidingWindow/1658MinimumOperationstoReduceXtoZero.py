class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, right, n = 0, 0, len(nums)
        total = sum(nums)
        if x > total:
            return -1
        target = total - x
        s, ans = 0, -1

        for right in range(n):
            s += nums[right]

            while left <= right and s > target:
                s -= nums[left]
                left += 1

            if s == target:
                ans = max(ans, right - left + 1)

        if ans == -1:
            return -1
        return n - ans



