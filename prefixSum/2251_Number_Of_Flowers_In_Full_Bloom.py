from bisect import bisect_right, bisect_left


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = []
        end = []
        for s, e in flowers:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        res = []
        # number of flowers blooming on ith day=number of flowers bloomed before ith day - number of flowers stopped blooming before ith day
        for x in people:
            res.append(bisect_right(start, x) - bisect_left(end, x))

        return res

