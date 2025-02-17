class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        sum, msum, tsum = 0, 99999999999, 0
        left, right = 0, 0
        n = len(card)

        while right < n - k:
            tsum += card[right]
            sum += card[right]
            right += 1

        msum = min(msum, sum)

        while (right < n):
            tsum += card[right]
            sum -= card[left]
            left += 1
            sum += card[right]
            right += 1
            msum = min(msum, sum)
        # print(msum,tsum)
        return tsum - msum
