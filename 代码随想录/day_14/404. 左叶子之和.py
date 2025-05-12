# 404. 左叶子之和
# https://leetcode.cn/problems/sum-of-left-leaves/
# https://programmercarl.com/0404.%E5%B7%A6%E5%8F%B6%E5%AD%90%E4%B9%8B%E5%92%8C.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 空树
        if root is None:
            return 0
        # 叶子节点
        if root.left is None and root.right is None:
            return 0
        # 左子树的左叶子之和
        if root.left and (root.left.left is None and root.left.right is None):
            left_sum = root.left.val
        else:
            left_sum = self.sumOfLeftLeaves(root.left)
        # 右子树的左叶子之和
        right_sum = self.sumOfLeftLeaves(root.right)
        return left_sum + right_sum
            