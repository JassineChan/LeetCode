# 202. 快乐数
# https://leetcode.cn/problems/happy-number/
# https://programmercarl.com/0202.%E5%BF%AB%E4%B9%90%E6%95%B0.html

class Solution:
    def isHappy(self, n: int) -> bool:
        # # 哈希表
        # appearence = set()
        # while True:
        #     if n == 1:
        #         return True
        #     count = 0
        #     while n > 0:
        #         num = n % 10
        #         count += num ** 2
        #         n = n // 10
        #     if count in appearence:
        #         return False
        #     appearence.add(count)
        #     n = count

        # 隐式链表：快慢双指针
        def getNext(n):
            count = 0
            while n > 0:
                num = n % 10
                count += num ** 2
                n = n // 10
            return count
        # 注意这里fast不能初始化为n
        fast, slow = getNext(n), n
        while fast != 1 and fast != slow:
            fast = getNext(getNext(fast))
            slow = getNext(slow)
        if fast == 1:
            return True
        else:
            return False