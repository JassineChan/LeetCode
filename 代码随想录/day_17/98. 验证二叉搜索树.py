# 98. 验证二叉搜索树
# https://leetcode.cn/problems/validate-binary-search-tree/
# https://programmercarl.com/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # min_val和max_val用于限制左右子树节点的值
    def check(self, root, min_val, max_val):
        if root == None:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        return self.check(root.left, min_val, root.val) and \
            self.check(root.right, root.val, max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val, max_val = -2 ** 32, 2 ** 32
        return self.check(root.left, min_val, root.val) and \
            self.check(root.right, root.val, max_val)