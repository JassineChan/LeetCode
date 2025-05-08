# 94. 二叉树的中序遍历
# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# class Solution:
#     def inorder(self, root, ans):
#         if root == None:
#             return 
#         self.inorder(root.left, ans)
#         ans.append(root.val)
#         self.inorder(root.right, ans)
#         return

#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         self.inorder(root, ans)
#         return ans

# 迭代
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        ans = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                ans.append(node.val)
                cur = node.right
        return ans