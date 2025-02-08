class MyCalendar:

    def __init__(self):
        self.nums = SortedDict()

    def book(self, start: int, end: int) -> bool:
        # BASIC

        # for s,e in self.nums:
        # if the guy who has come late comes befor the girl who is leaving earlier then they will meet
        #     if max(s,start)<min(e,end):
        #         return False

        # self.nums.append([start,end])
        # return True

        # OPTIMIZED

        # if start in self.nums:
        #     self.nums[start]+=1
        # else:
        #     self.nums[start]=1

        # if end in self.nums:
        #     self.nums[end]-=1
        # else:
        #     self.nums[end]=-1
        # sum=0
        # for key,values in self.nums.items():
        #     sum+=values
        #     if sum>1:
        #         self.nums[start]-=1
        #         self.nums[end]+=1
        #         return False
        # return True

        # highlyOptimized

        # returns the next greater elemnts index
        index = self.nums.bisect_right(start)

        if index > 0 and self.nums.peekitem(index - 1)[1] > start:
            return False
        if index < len(self.nums) and self.nums.peekitem(index)[0] < end:
            return False

        self.nums[start] = end
        return True





