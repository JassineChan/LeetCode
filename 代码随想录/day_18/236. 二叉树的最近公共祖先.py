# 236. 二叉树的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# https://programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, root, p, q):
        if root == None:
            return None
        if root == p or root == q:
            return root
        left_ans = self.postorder(root.left, p, q)
        right_ans = self.postorder(root.right, p, q)
        if left_ans and right_ans:
            return root
        elif left_ans:
            return left_ans
        elif right_ans:
            return right_ans
        else:
            return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 后序遍历
        ans = self.postorder(root, p, q)
        return ans
