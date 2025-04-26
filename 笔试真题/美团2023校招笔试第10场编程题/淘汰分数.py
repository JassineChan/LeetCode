import sys

n_x_y = sys.stdin.readline().strip().split()
n, x, y = int(n_x_y[0]), int(n_x_y[1]), int(n_x_y[2])
nums = sys.stdin.readline().strip().split()
for i in range(n):
    nums[i] = int(nums[i])
nums = sorted(nums)
ans = -1
for i in range(n):
    if x <= i+1 <= y and x <= n-i-1 <= y:
        ans = nums[i]
        break
print(ans)