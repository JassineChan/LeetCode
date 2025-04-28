# 349. 两个数组的交集
# https://leetcode.cn/problems/intersection-of-two-arrays/
# https://programmercarl.com/0349.%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E7%9A%84%E4%BA%A4%E9%9B%86.html

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
        