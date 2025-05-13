# 530. 二叉搜索树的最小绝对差
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/
# https://programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root == None:
            return 
        self.inorder(root.left)
        if self.pre:
            self.ans = min(self.ans, root.val-self.pre.val)
        self.pre = root
        self.inorder(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # # 迭代中序遍历
        # ans = 10 ** 5
        # stack = []
        # pre, cur = None, root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     if pre:
        #         ans = min(ans, cur.val-pre.val)
        #     pre = cur
        #     cur = cur.right
        # return ans

        # 递归法
        self.ans = 10 ** 5
        self.pre = None
        self.inorder(root)
        return self.ans
