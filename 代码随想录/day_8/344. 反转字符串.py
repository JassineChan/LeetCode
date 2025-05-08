# 344. 反转字符串
# https://leetcode.cn/problems/reverse-string/
# https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针
        s_len = len(s)
        left, right = 0, s_len-1 
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return   