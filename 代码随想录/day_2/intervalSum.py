# 58. 区间和（第九期模拟笔试）
# https://kamacoder.com/problempage.php?pid=1070
# https://www.programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html

import sys

n = int(sys.stdin.readline().strip())
nums = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    nums.append(num)
pre_sum = [0] * n
for i in range(1, n):
    pre_sum[i] = pre_sum[i-1] + nums[i-1]
while True:
    try:
        a_b = sys.stdin.readline().strip().split()
        a, b = int(a_b[0]), int(a_b[1])
        ans = pre_sum[b] - pre_sum[a] + nums[b]
        print(ans)
    except:
        break
