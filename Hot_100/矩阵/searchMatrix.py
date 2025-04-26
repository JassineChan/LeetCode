# 240. 搜索二维矩阵 II
# https://leetcode.cn/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 斜遍历
        m, n = len(matrix), len(matrix[0])
        # 从右上角开始
        row, col = 0, n-1
        while row < m and col > -1:
            # 如果目标大于当前值，往下走
            if target > matrix[row][col]:
                row += 1
            # 如果目标小于当前值，往左走
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True
        return False