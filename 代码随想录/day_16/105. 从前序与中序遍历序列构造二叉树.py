# 105. 从前序与中序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, preorder, inorder, in_num2idx, pre_start_idx, pre_end_idx, in_start_idx, in_end_idx):
        # 终止条件
        if in_end_idx < in_start_idx:
            return None
        # 先序遍历的起始节点是根节点
        root_num = preorder[pre_start_idx]
        in_root_idx = in_num2idx[root_num]
        # 左树节点数
        left_tree_len = in_root_idx-in_start_idx
        # 创建根节点
        root = TreeNode(root_num)
        root.left = self.build(preorder, inorder, in_num2idx, pre_start_idx+1, pre_start_idx+left_tree_len, in_start_idx, in_root_idx-1)
        root.right = self.build(preorder, inorder, in_num2idx, pre_start_idx+left_tree_len+1, pre_end_idx, in_root_idx+1, in_end_idx)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # # 先序: [ 根节点, [左子树的前序遍历结果], [右子树的前序遍历结果] ]
        # # 中序: [ [左子树的中序遍历结果], 根节点, [右子树的中序遍历结果] ]
        # n = len(preorder)
        # in_val2index = {val: index for index, val in enumerate(inorder)}
        # # 递归构造, 左闭右闭
        # def fun(pre_left, pre_right, in_left, in_right):
        #     if pre_left > pre_right:
        #         return None
        #     pre_root_val_idx = pre_left
        #     in_root_val_idx = in_val2index[preorder[pre_root_val_idx]]
        #     root = TreeNode(preorder[pre_root_val_idx])
        #     left_tree_size = in_root_val_idx - in_left
        #     root.left = fun(
        #         pre_left + 1, 
        #         pre_left + left_tree_size,
        #         in_left,
        #         in_root_val_idx - 1
        #     )
        #     root.right = fun(
        #         pre_left + left_tree_size + 1,
        #         pre_right,
        #         in_root_val_idx + 1,
        #         in_right
        #     )
        #     return root
        
        # root = fun(0, n-1, 0, n-1)
        # return root

        in_num2idx = {}
        for idx, num in enumerate(inorder):
            in_num2idx[num] = idx
        root = self.build(preorder, inorder, in_num2idx, 0, len(preorder)-1, 0, len(inorder)-1)
        return root