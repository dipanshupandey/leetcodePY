class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        first_row = any(matrix[0][i] == 0 for i in range(col))
        first_col = any(matrix[i][0] == 0 for i in range(row))

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row == True:
            for i in range(col):
                matrix[0][i] = 0

        if first_col == True:
            for i in range(row):
                matrix[i][0] = 0

        # print(matrix)
