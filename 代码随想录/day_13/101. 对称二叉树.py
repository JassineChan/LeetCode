# 101. 对称二叉树
# https://leetcode.cn/problems/symmetric-tree/
# https://programmercarl.com/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    def check(self, left_tree, right_tree):
        # 均为空树
        if left_tree == None and right_tree == None:
            return True
        # 一个空树, 一个非空
        if left_tree == None or right_tree == None:
            return False
        # 判断节点值是否相等
        if left_tree.val != right_tree.val:
            return False
        return self.check(left_tree.left, right_tree.right) and \
            self.check(left_tree.right, right_tree.left)

    # 迭代
    def check_iter(self, left_tree, right_tree):
        from collections import deque
        queue = deque()
        queue.append(left_tree)
        queue.append(right_tree)
        while queue:
            left_tree = queue.popleft()
            right_tree = queue.popleft()
            if left_tree == None and right_tree == None:
                continue
            if left_tree == None or right_tree == None:
                return False
            if left_tree.val != right_tree.val:
                return False
            queue.append(left_tree.left)
            queue.append(right_tree.right)
            queue.append(left_tree.right)
            queue.append(right_tree.left)
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 如果同时满足下面的条件，两个树互为镜像：
        # 它们的两个根结点具有相同的值
        # 每个树的右子树都与另一个树的左子树镜像对称
        # return self.check(root.left, root.right)
        return self.check_iter(root.left, root.right)