# 654. 最大二叉树
# https://leetcode.cn/problems/maximum-binary-tree/
# https://programmercarl.com/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 模拟
    def build(self, nums, start, end):
        if end <= start:
            return None
        root_idx = start
        for i in range(start+1, end):
            if nums[i] > nums[root_idx]:
                root_idx = i
        root = TreeNode(nums[root_idx])
        root.left = self.build(nums, start, root_idx)
        root.right = self.build(nums, root_idx+1, end)
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # # 左闭右开
        # root = self.build(nums, 0, len(nums))
        # return root

        # 单调递减栈(一次遍历)
        min_stack = []
        nums_len = len(nums)
        # 存放树的所有节点
        tree = [None] * nums_len
        for i in range(nums_len):
            tree[i] = TreeNode(nums[i])
            while min_stack and nums[i] > nums[min_stack[-1]]:
                idx = min_stack.pop()
                tree[i].left = tree[idx]
            if min_stack:
                tree[min_stack[-1]].right = tree[i]
            min_stack.append(i)
        return tree[min_stack[0]]
            