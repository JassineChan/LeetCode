# 145. 二叉树的后序遍历
# https://leetcode.cn/problems/binary-tree-postorder-traversal/
# https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归
# class Solution:
#     def postorder(self, root, ans):
#         if root == None:
#             return
#         self.postorder(root.left, ans)
#         self.postorder(root.right, ans)
#         ans.append(root.val)

#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         self.postorder(root, ans)
#         return 

# 迭代
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        # 左右中 -> 中右左逆序 -> 类先序遍历
        ans = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        ans = ans[::-1]
        return ans