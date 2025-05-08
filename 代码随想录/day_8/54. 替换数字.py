# 54. 替换数字（第八期模拟笔试）
# https://kamacoder.com/problempage.php?pid=1064

import sys

s = sys.stdin.readline().strip()
ans = ""
for i in range(len(s)):
    if ord("a") <= ord(s[i]) <= ord("z"):
        ans += s[i]
    else:
        ans += "number"
print(ans)