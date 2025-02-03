class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        res=list(range(n))
        same=0
        high=n
        low=0
        for x in nums:
            if x<pivot:
                same+=1
            elif x>pivot:
                high-=1

        for x in nums:
            if x<pivot:
                res[low]=x
                low+=1
            elif x==pivot:
                res[same]=x
                same+=1
            else:
                res[high]=x
                high+=1

        return res