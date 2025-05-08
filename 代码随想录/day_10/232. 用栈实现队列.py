# 232. 用栈实现队列
# https://leetcode.cn/problems/implement-queue-using-stacks/
# https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if self.out_stack:
            x = self.out_stack.pop()
            return x
        else:
            while self.in_stack:
                tmp = self.in_stack.pop()
                self.out_stack.append(tmp)
            x = self.out_stack.pop()
            return x

    def peek(self) -> int:
        if self.out_stack:
            x = self.out_stack[-1]
            return x
        else:
            while self.in_stack:
                tmp = self.in_stack.pop()
                self.out_stack.append(tmp)
            x = self.out_stack[-1]
            return x
        
    def empty(self) -> bool:
        if self.in_stack or self.out_stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()