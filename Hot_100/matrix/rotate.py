# 48. 旋转图像
# https://leetcode.cn/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        loops = n // 2
        for loop in range(loops):
            row, col = loop, loop
            while col < n-loop-1:
                tmp = matrix[row][col]
                matrix[row][col] = matrix[n-col-1][row]
                matrix[n-col-1][row] = matrix[n-row-1][n-col-1]
                matrix[n-row-1][n-col-1] = matrix[col][n-row-1]
                matrix[col][n-row-1] = tmp
                col += 1
