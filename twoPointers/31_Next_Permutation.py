class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first of all we will search for first decreasing index from right because we need to find the smallest greater permutaion
        n = len(nums)
        i = n - 1
        j = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        # we didt find any decreasing index that means the array is in decreasing order or the largest pemutation we can have so we sort
        if i == 0:
            nums.sort()
            return
        i -= 1
        # we have to find the smallest element which is greater than the element at index i to find the smallest greater permutation
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        # swap both indexes

        nums[i], nums[j] = nums[j], nums[i]

        # now reverse the elements after index i to make it smalles greater array
        nums[i + 1 :] = reversed(nums[i + 1 :])
