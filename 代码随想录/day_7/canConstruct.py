# 383. 赎金信
# https://leetcode.cn/problems/ransom-note/
# https://programmercarl.com/0383.%E8%B5%8E%E9%87%91%E4%BF%A1.html

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 数组哈希表
        r_chars = [0] * 26
        for i in range(len(magazine)):
            r_chars[ord(magazine[i]) - ord("a")] += 1
        for i in range(len(ransomNote)):
            index = ord(ransomNote[i]) - ord("a")
            r_chars[index] -= 1
            if r_chars[index] < 0:
                return False
        return True