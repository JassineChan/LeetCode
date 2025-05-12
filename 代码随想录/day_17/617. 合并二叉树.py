# 617. 合并二叉树
# https://leetcode.cn/problems/merge-two-binary-trees/
# https://programmercarl.com/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, root1, root2):
        if not root1 and not root2:
            return None
        elif not root1:
            return root2
        elif not root2:
            return root1
        root1.val += root2.val
        root1.left = self.merge(root1.left, root2.left)
        root1.right = self.merge(root1.right, root2.right)
        return root1

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.merge(root1, root2)
        return root