# 110. 平衡二叉树
# https://leetcode.cn/problems/balanced-binary-tree/
# https://programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if root is None:
            return 0
        left_height = self.getHeight(root.left)
        # 左子树是非平衡二叉树
        if left_height == -1:
            return -1
        right_height = self.getHeight(root.right)
        # 右子树是非平衡二叉树
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            # -1表示非平衡二叉树
            return -1
        return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) == -1:
            return False
        else:
            return True