# 242. 有效的字母异位词
# https://leetcode.cn/problems/valid-anagram/
# https://programmercarl.com/0242.%E6%9C%89%E6%95%88%E7%9A%84%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.html

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 哈希表
        # s_chars = [0] * 26
        # for i in range(len(s)):
        #     s_chars[ord(s[i]) - ord("a")] += 1
        # for i in range(len(t)):
        #     s_chars[ord(t[i]) - ord("a")] -= 1
        # for i in range(len(s_chars)):
        #     if s_chars[i] != 0:
        #         return False
        # return True

        # 如果包含 unicode 字符(一个字符可能对应多个字节、字符是离散未知的)
        from collections import defaultdict
        hash_map = defaultdict(int)
        for i in range(len(s)):
            hash_map[s[i]] += 1
        for i in range(len(t)):
            hash_map[t[i]] -= 1
        for key, value in hash_map.items():
            if value != 0:
                return False
        return True 
