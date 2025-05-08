# 20. 有效的括号
# https://leetcode.cn/problems/valid-parentheses/
# https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html

class Solution:
    def isValid(self, s: str) -> bool:
        left2right = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        s_len = len(s)
        for i in range(s_len):
            if s[i] in left2right:
                stack.append(left2right[s[i]])
            else:
                if stack and s[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True