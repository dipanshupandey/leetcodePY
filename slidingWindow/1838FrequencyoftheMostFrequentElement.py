class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        right, left, n = 0, 0, len(nums)
        total_sum = 0
        nums.sort()
        ans = 0
        for right in range(n):
            total_sum += nums[right]
            increment = nums[right] * (right - left + 1) - total_sum
            while increment > k:
                total_sum -= nums[left]
                left += 1
                increment = nums[right] * (right - left + 1) - total_sum
            ans = max(ans, right - left + 1)

        return ans


