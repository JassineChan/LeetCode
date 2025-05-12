# 257. 二叉树的所有路径
# https://leetcode.cn/problems/binary-tree-paths/
# https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_search(self, root, ans, path):
        if root == None:
            return
        # 将当前节点添加到路径中
        path.append(str(root.val))
        # 到达叶子节点, 保存当前路径
        if root.left == None and root.right == None:
            ans.append("->".join(path))
        self.preorder_search(root.left, ans, path)
        self.preorder_search(root.right, ans, path)
        # 回溯, 把当前节点从路径中删除
        path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans, path = [], []
        self.preorder_search(root, ans, path)
        return ans