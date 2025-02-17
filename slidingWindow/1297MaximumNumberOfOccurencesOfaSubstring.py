class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        mp = defaultdict(int)
        mp2 = defaultdict(int)
        left, n = 0, len(s)
        temp = ""
        c = 0
        res = 0
        for i in range(n):
            temp += s[i]
            mp2[s[i]] += 1
            if mp2[s[i]] == 1:
                c += 1
            if i - left + 1 == minSize:
                if c <= maxLetters:
                    mp[temp] += 1
                    res = max(res, mp[temp])
                temp = temp[1:]

                mp2[s[left]] -= 1
                if mp2[s[left]] == 0:
                    c -= 1
                left += 1

        return res


