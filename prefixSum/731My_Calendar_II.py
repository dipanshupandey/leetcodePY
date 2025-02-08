class MyCalendarTwo:

    def __init__(self):
        self.nums = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if start in self.nums:
            self.nums[start] += 1
        else:
            self.nums[start] = 1

        if end in self.nums:
            self.nums[end] -= 1
        else:
            self.nums[end] = -1

        sum = 0
        for key, values in self.nums.items():
            sum += values
            if sum > 2:
                # print(self.nums)
                self.nums[start] -= 1
                self.nums[end] += 1
                return False

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)