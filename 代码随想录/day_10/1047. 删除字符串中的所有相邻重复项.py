# 1047. 删除字符串中的所有相邻重复项
# https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/
# https://programmercarl.com/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.html

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s_len = len(s)
        for i in range(s_len):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)