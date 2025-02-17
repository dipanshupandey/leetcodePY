class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        high,low,n,res,m=0,0,len(nums),0,0

        for high in range(n):
            if nums[high]>right:
                m=0
                low=high+1
            elif nums[high]<left:
                res+=m
            else:
                m=high-low+1
                res+=m

        return res