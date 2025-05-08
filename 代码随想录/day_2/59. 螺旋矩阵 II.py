# 59. 螺旋矩阵 II
# https://leetcode.cn/problems/spiral-matrix-ii/
# https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html
# https://www.bilibili.com/video/BV1SL4y1N7mV/
# 注意：本题与 54 题相似，题目要求返回的是顺时针填充的矩阵，而不是顺时针打印的矩阵。

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 这里不能使用[[0] * n] * n
        # 会导致所有行指向同一个内存中的子列表
        # ans = [[0] * n] * n
        # ans[0][0] = 1 # 修改一个元素
        # 输出: [[1, 0, 0], [1, 0, 0], [1, 0, 0]] (所有行的第一个元素都被修改了！)
        # 下面的代码在每次迭代都会生成一个新的子列表，确保每一行独立
        ans = [[0 for _ in range(n)] for _ in range(n)]
        row, col = 0, 0
        # 循环次数
        loop = n // 2
        # 当前填充值
        cur_num = 1
        # 在模拟时，要注意循环不变量
        # 即对于四个角落的值的处理统一
        for k in range(loop):
            row, col = k, k
            while col < n-k-1:
                ans[row][col] = cur_num
                cur_num += 1
                col += 1
            while row < n-k-1:
                ans[row][col] = cur_num
                cur_num += 1
                row += 1
            while col > k:
                ans[row][col] = cur_num
                cur_num += 1
                col -= 1
            while row > k:
                ans[row][col] = cur_num
                cur_num += 1
                row -= 1
        # 如果n为奇数，需填充中间位置的值
        if n % 2 == 1:
            ans[loop][loop] = cur_num
        return ans