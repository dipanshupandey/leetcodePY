class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        row = len(self.m)
        col = len(self.m[0])
        self.prefix = [[0] * col for r in range(row)]

        for i in range(row):
            p = 0
            for j in range(col):
                p += self.m[i][j]
                self.prefix[i][j] = p

        for i in range(col):
            p = 0

            for j in range(row):
                p += self.prefix[j][i]
                self.prefix[j][i] = p

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]

        if row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1 - 1]

        if col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1 - 1][col2]

        return self.prefix[row2][col2] - (
                    self.prefix[row1 - 1][col2] + self.prefix[row2][col1 - 1] - self.prefix[row1 - 1][col1 - 1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)