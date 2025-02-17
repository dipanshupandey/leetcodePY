class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right, n, res = 0, 0, len(nums), 0
        product = 1
        if k < 0:
            return 0

        for right in range(n):
            product *= nums[right]

            while left <= right and product >= k:
                product //= nums[left]
                left += 1

            res += (right - left + 1)

        return res
