import sys

n = int(sys.stdin.readline().strip())
nums = sys.stdin.readline().strip().split()
for i in range(n):
    nums[i] = int(nums[i])
nums = sorted(nums)
ans = 0
for i in range(n):
    ans += abs(nums[i] - (i+1))
print(ans)