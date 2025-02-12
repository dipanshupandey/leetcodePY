class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        # subarray between i to j = prefix[j]-prefix[i-1], subarray divisible by k means
        # ((prefix[j])-(prefix[i])) % k=0
        #   prefix[j]%k = prefix[i]%k by evaluating
        # that meand if two subarrays have equal remider that means the subarray is divisible by k so we will keep storing remainder
        for x in nums:
            prefix += x
            mod = prefix % k
            if mod < 0:
                mod *= -1
            if count[mod]:
                res += count[mod]
            count[mod] += 1

        return res

