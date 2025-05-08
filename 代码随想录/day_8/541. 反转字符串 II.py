# 541. 反转字符串 II
# https://leetcode.cn/problems/reverse-string-ii/
# https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # # 模拟
        # s_len = len(s)
        # ans = ""
        # flag = True
        # for i in range(0, s_len, k):
        #     if flag:
        #         for j in range(min(i+k-1, s_len-1), i-1, -1):
        #             ans += s[j]
        #         flag = False
        #     else:
        #         for j in range(i, min(i+k, s_len)):
        #             ans += s[j]
        #         flag = True
        # return ans   

        # 模拟
        s_len = len(s)
        s_list = list(s)
        for i in range(0, s_len, 2*k):
            s_list[i:i+k] = reversed(s_list[i:i+k])
        return "".join(s_list)