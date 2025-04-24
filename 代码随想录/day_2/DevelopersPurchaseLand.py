# 44. 开发商购买土地（第五期模拟笔试）
# https://kamacoder.com/problempage.php?pid=1044
# https://www.programmercarl.com/kamacoder/0044.%E5%BC%80%E5%8F%91%E5%95%86%E8%B4%AD%E4%B9%B0%E5%9C%9F%E5%9C%B0.html

import sys

n_m = sys.stdin.readline().strip().split()
n, m = int(n_m[0]), int(n_m[1])
matrix = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    nums = sys.stdin.readline().strip().split()
    for j in range(m):
        matrix[i][j] = int(nums[j])
# 行数组前缀和
row_pre_sum = [[0 for _ in range(m + 1)] for _ in range(n)]
for i in range(n):
    for j in range(1, m+1):
        row_pre_sum[i][j] = row_pre_sum[i][j-1] + matrix[i][j-1]
# 列数组前缀和
col_pre_sum = [[0 for _ in range(m)] for _ in range(n + 1)]
for j in range(m):
    for i in range(1, n+1):
        col_pre_sum[i][j] = col_pre_sum[i-1][j] + matrix[i-1][j]

ans = sys.maxsize
# 横切
for i in range(1, n):
    A, B = 0, 0
    for j in range(m):
        A += col_pre_sum[i][j]
        B += (col_pre_sum[n][j] - col_pre_sum[i][j])
    ans = min(ans, abs(A - B)) 

# 竖切
for j in range(1, m):
    A, B = 0, 0
    for i in range(n):
        A += row_pre_sum[i][j]
        B += (row_pre_sum[i][m] - row_pre_sum[i][j])
    ans = min(ans, abs(A - B))
print(ans)