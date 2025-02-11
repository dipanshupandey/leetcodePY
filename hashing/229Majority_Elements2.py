class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2, vote1, vote2 = None, None, 0, 0

        for x in nums:
            if vote1 == 0 and x != candidate2:
                candidate1 = x
            elif vote2 == 0 and x != candidate1:
                candidate2 = x

            if x == candidate1:
                vote1 += 1
            elif x == candidate2:
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1

        c1, c2 = 0, 0

        for x in nums:
            if x == candidate1:
                c1 += 1
            elif x == candidate2:
                c2 += 1

        res = []

        if c1 > len(nums) // 3:
            res.append(candidate1)
        if c2 > len(nums) // 3:
            res.append(candidate2)
        return res