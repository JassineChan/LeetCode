# 538. 把二叉搜索树转换为累加树
# https://leetcode.cn/problems/convert-bst-to-greater-tree/
# https://programmercarl.com/0538.%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%B4%AF%E5%8A%A0%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def re_inorder(self, root):
        if not root:
            return
        self.re_inorder(root.right)
        root.val += self.count
        self.count = root.val
        self.re_inorder(root.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.count = 0
        self.re_inorder(root)
        return root