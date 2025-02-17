class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right = 0, 0
        sum = 0
        res, n = 0, len(arr)

        for right in range(k):
            sum += arr[right]

        if sum // k >= threshold:
            res += 1

        for right in range(k, n):
            sum -= arr[left]
            left += 1
            sum += arr[right]
            right += 1
            if sum // k >= threshold:
                res += 1

        return res
