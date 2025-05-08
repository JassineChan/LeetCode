# 515. 在每个树行中找最大值
# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        from collections import deque
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            max_num = -2 ** 31
            for _ in range(len(queue)):
                node = queue.popleft()
                max_num = max(max_num, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_num)
        return ans
