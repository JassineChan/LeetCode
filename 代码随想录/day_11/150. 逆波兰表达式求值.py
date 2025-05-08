# 150. 逆波兰表达式求值
# https://leetcode.cn/problems/evaluate-reverse-polish-notation/
# https://programmercarl.com/150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。
        stack = []
        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(int(num1 / num2))
        return stack[0]
