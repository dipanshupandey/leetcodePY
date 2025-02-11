from collections import defaultdict
class Solution:
    #Boyer Moore voting algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=-1
        for x in nums:
            if count==0:
                candidate=x

            if candidate==x:
                count+=1
            else:
                count-=1

        return candidate