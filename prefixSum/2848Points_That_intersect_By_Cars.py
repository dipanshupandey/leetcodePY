class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        res=0
        start=nums[0][0]
        end=nums[0][1]

        for x in nums:
            if x[0]<=end:
                start=min(x[0],start)
                end=max(x[1],end)
            else:
                res+=(end-start+1)
                start=x[0]
                end=x[1]
        res+=(end-start+1)
        return res
