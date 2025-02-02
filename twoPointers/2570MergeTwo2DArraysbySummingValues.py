class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # x=0
        # y=0
        # res=[]
        # while x<len(nums1) and y<len(nums2):
        #     if nums1[x][0]==nums2[y][0]:
        #         res.append([nums1[x][0],nums1[x][1]+nums2[y][1]])
        #         # print(nums1[x][1]+nums2[y][1])
        #         x+=1
        #         y+=1
        #     elif nums1[x][0]<nums2[y][0]:
        #         res.append(nums1[x])
        #         x+=1
        #     else:
        #         res.append(nums2[y])
        #         y+=1

        # while(x<len(nums1)):
        #     res.append(nums1[x])
        #     x+=1

        # while(y<len(nums2)):
        #     res.append(nums2[y])
        #     y+=1

        # return res

        res = defaultdict(int)

        for x, t in nums1:
            res[x] += t

        for x, t in nums2:
            res[x] += t
        # print(res.items())
        return sorted(res.items())