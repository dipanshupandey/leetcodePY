class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        left = 0
        right = 0
        count = 0
        res = 0
        while right < k:
            if s[right] in vowels:
                count += 1
            res = max(count, res)
            right += 1

        while right < n:
            if s[left] in vowels:
                count -= 1
            left += 1

            if s[right] in vowels:
                count += 1
            right += 1

            res = max(count, res)

        return res

