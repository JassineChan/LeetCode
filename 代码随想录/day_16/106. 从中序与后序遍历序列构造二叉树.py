# 106. 从中序与后序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, inorder, postorder, in_num2idx, in_start_idx, in_end_idx, post_start_idx, post_end_idx):
        # 终止条件: 空节点
        if in_end_idx < in_start_idx:
            return None
        # 后序遍历的终止节点是根节点
        root_num = postorder[post_end_idx]
        in_root_idx = in_num2idx[root_num]
        # 左子树节点数
        left_tree_len = in_root_idx-in_start_idx
        # 创建树根节点
        root = TreeNode(root_num)
        root.left = self.build(inorder, postorder, in_num2idx, in_start_idx, in_root_idx-1, post_start_idx, post_start_idx+left_tree_len-1)
        root.right = self.build(inorder, postorder, in_num2idx, in_root_idx+1, in_end_idx, post_start_idx+left_tree_len, post_end_idx-1)
        return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_num2idx = {}
        for idx, num in enumerate(inorder):
            in_num2idx[num] = idx
        root = self.build(inorder, postorder, in_num2idx, 0, len(inorder)-1, 0, len(postorder)-1)
        return root