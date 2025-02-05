class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        right = 1
        # first we are finding product of elements before the ith index that is product of element left from ith index
        for i in range(n):
            res[i] = left
            left *= nums[i]
        # then we are multiplying product of elements left from ith index to the product of elements right from ith index
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
