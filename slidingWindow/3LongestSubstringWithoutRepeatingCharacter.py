class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        left, right, ans, n = 0, 0, 0, len(s)

        while right < n:
            mp[s[right]] += 1

            while (mp[s[right]] > 1):
                mp[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans

