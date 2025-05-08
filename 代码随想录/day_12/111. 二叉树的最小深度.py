# 111. 二叉树的最小深度
# https://leetcode.cn/problems/minimum-depth-of-binary-tree/
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html

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
        if root.left == None and root.right != None:
            return right_depth + 1
        if root.left != None and root.right == None:
            return left_depth + 1
        return min(left_depth, right_depth) + 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # return self.getDepth(root)
        if root == None:
            return 0
        from collections import deque
        ans = 0
        queue = deque()
        queue.append(root)
        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left == None and node.right == None:
                    return ans
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)