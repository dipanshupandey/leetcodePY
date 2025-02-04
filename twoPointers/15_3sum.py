class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            start = i + 1
            end = n - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < n and nums[start] == nums[start - 1]:
                        start += 1
                    end -= 1
                    while end >= 0 and nums[end] == nums[end + 1]:
                        end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                    while start < n and nums[start] == nums[start - 1]:
                        start += 1
                else:
                    end -= 1
                    while end >= 0 and nums[end] == nums[end + 1]:
                        end -= 1

        return res