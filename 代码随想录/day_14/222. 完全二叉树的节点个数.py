# 222. 完全二叉树的节点个数
# https://leetcode.cn/problems/count-complete-tree-nodes/
# https://programmercarl.com/0222.%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%AA%E6%95%B0.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # 最左深度和最右深度
        left_depth, right_depth = 1, 1
        left, right = root.left, root.right
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            return 2 ** left_depth - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
