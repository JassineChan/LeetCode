# 225. 用队列实现栈
# https://leetcode.cn/problems/implement-stack-using-queues/
# https://programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html

# 两个队列
# class MyStack:

#     def __init__(self):
#         from collections import deque
#         self.queue1 = deque()
#         self.queue2 = deque()

#     def push(self, x: int) -> None:
#         self.queue1.append(x)

#     def pop(self) -> int:
#         for _ in range(len(self.queue1)-1):
#             tmp = self.queue1.popleft()
#             self.queue2.append(tmp)
#         x = self.queue1.popleft()
#         self.queue1, self.queue2 = self.queue2, self.queue1
#         return x

#     def top(self) -> int:
#         for _ in range(len(self.queue1)):
#             tmp = self.queue1.popleft()
#             self.queue2.append(tmp)
#         x = self.queue2[-1]
#         self.queue1, self.queue2 = self.queue2, self.queue1
#         return x

#     def empty(self) -> bool:
#         if self.queue1 or self.queue2:
#             return False
#         else:
#             return True


# 一个队列
class MyStack:

    def __init__(self):
        from collections import deque
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue)-1):
            tmp = self.queue.popleft()
            self.queue.append(tmp)
        x = self.queue.popleft()
        return x

    def top(self) -> int:
        for _ in range(len(self.queue)):
            tmp = self.queue.popleft()
            self.queue.append(tmp)
        x = self.queue[-1]
        return x

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()