# 54. 螺旋矩阵
# https://leetcode.cn/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        k = min(m, n)
        # 完整的循环次数
        loops = k // 2
        # 注意循环不变量
        for loop in range(loops):
            row, col = loop, loop
            # 上
            while col < n-loop-1:
                ans.append(matrix[row][col])
                col += 1
            # 右
            while row < m-loop-1:
                ans.append(matrix[row][col])
                row += 1
            # 下
            while col > loop:
                ans.append(matrix[row][col])
                col -= 1
            # 左
            while row > loop:
                ans.append(matrix[row][col])
                row -= 1
        # 如果k为奇数，最后剩下一点、一行或者一列
        if k % 2 == 1:
            row, col = loops, loops
            if m == n:
                ans.append(matrix[row][col])
            elif n > m:
                while col < n-loops:
                    ans.append(matrix[row][col])
                    col += 1
            else:
                while row < m-loops:
                    ans.append(matrix[row][col])
                    row += 1
        return ans