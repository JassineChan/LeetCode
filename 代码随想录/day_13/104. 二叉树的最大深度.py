# 104. 二叉树的最大深度
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root):
        if root == None:
            return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        return 1 + max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max_depth = self.getDepth(root)
        from collections import deque
        if root == None:
            return 0
        queue = deque()
        max_depth = 0
        queue.append(root)
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth