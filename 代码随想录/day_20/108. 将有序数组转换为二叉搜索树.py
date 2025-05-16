# 108. 将有序数组转换为二叉搜索树
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
# https://programmercarl.com/0108.%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_tree(self, nums, left_idx, right_idx):
        if left_idx > right_idx:
            return None
        mid_idx = left_idx + (right_idx - left_idx) // 2
        root = TreeNode(nums[mid_idx])
        root.left = self.build_tree(nums, left_idx, mid_idx-1)
        root.right = self.build_tree(nums, mid_idx+1, right_idx)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 数组是二叉搜索树的中序遍历序列
        return self.build_tree(nums, 0, len(nums)-1) 