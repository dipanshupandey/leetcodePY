class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # res=nums
        # res=res[0:n-k][::-1]+res[n-k:][::-1]
        # res=res[::-1]
        # for i in range(n):
        #     nums[i]=res[i]

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
