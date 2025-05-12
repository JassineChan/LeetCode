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
        # 栈中存放的是节点在 nums 中的索引
        min_stack = []
        nums_len = len(nums)
        # 创建一个与 nums 对应的 TreeNode 列表
        tree_nodes = [TreeNode(num) for num in nums]
        for i in range(nums_len):
            # 当前元素比栈顶的元素大，弹出栈顶元素并将其作为当前节点的左子节点
            while min_stack and nums[i] > nums[min_stack[-1]]:
                idx = min_stack.pop()
                tree[i].left = tree[idx]
            # 如果栈不为空，当前节点应是栈顶节点的右子节点
            if min_stack:
                tree[min_stack[-1]].right = tree[i]
            # 当前节点入栈
            min_stack.append(i)
        # 最后栈底的索引是根节点的位置
        return tree[min_stack[0]]
            