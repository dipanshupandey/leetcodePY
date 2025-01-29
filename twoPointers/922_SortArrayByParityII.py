class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # odd=[x for x in nums if x % 2==1]
        # even=[x for x in nums if x % 2==0]
        # res=[]
        # for e,o in zip(even,odd):
        #     res.append(e)
        #     res.append(o)
        # return res

        oddIndex = 1
        evenIndex = 0
        n = len(nums)
        while evenIndex < n and oddIndex < n:
            if nums[evenIndex] % 2 == 0:
                evenIndex += 2
            elif nums[oddIndex] % 2 == 1:
                oddIndex += 2
            else:
                nums[evenIndex], nums[oddIndex] = nums[oddIndex], nums[evenIndex]
                oddIndex += 2
                evenIndex += 2

        return nums