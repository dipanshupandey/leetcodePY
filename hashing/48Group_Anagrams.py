from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            char_count = [0] * 26

            for char in word:
                char_count[ord(char) - ord('a')] += 1

            group[tuple(char_count)].append(word)

        print(group)

        return list(group.values())

        # dict=defaultdict(list)
        # for x in strs:
        #     temp="".join(sorted(x))
        #     # print(temp)
        #     dict[temp].append(x)

        # res=[]
        # for key,values in dict.items():
        #     res.append(values)

        # return res
