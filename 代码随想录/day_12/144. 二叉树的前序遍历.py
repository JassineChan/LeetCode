# 144. 二叉树的前序遍历
# https://leetcode.cn/problems/binary-tree-preorder-traversal/
# https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归
# class Solution:
#     def preorder(self, root, ans):
#         if root == None:
#             return
#         ans.append(root.val)
#         self.preorder(root.left, ans)
#         self.preorder(root.right, ans)
#         return 

#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         self.preorder(root, ans)
#         return ans
# 迭代
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        ans = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            # 先右
            if node.right:
                stack.append(node.right)
            # 后左
            if node.left:
                stack.append(node.left)
        return ans
        