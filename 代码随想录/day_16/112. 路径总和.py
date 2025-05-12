# 112. 路径总和
# https://leetcode.cn/problems/path-sum/
# https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            if root.val == targetSum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, targetSum-root.val) or \
            self.hasPathSum(root.right, targetSum-root.val)