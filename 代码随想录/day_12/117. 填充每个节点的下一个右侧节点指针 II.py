# 117. 填充每个节点的下一个右侧节点指针 II
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                node = queue.popleft()
                # if i == 0:
                #     pre = node
                # elif i == q_len-1:
                #     pre.next = node
                #     pre = pre.next
                #     node.next = None
                # else:
                #     pre.next = node
                #     pre = pre.next
                if i < q_len-1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root 