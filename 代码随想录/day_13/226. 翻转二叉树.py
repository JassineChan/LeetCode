# 226. 翻转二叉树
# https://leetcode.cn/problems/invert-binary-tree/
# https://programmercarl.com/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_reverse(self, root):
        if root == None:
            return 
        root.left, root.right = root.right, root.left
        self.preorder_reverse(root.left)
        self.preorder_reverse(root.right)
        return 

    def postorder_reverse(self, root):
        if root == None:
            return
        self.postorder_reverse(root.left)
        self.postorder_reverse(root.right)
        root.left, root.right = root.right, root.left
        return 

    def levelorder_reverse(self, root):
        if root == None:
            return
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def inorder_reverse(self, root):
        if root == None:
            return
        self.inorder_reverse(root.left)
        root.left, root.right = root.right, root.left
        # 中间节点翻转导致左右子树改变
        self.inorder_reverse(root.left)
        return

    # 只要把每一个节点的左右孩子翻转一下，就可以达到整体翻转的效果.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.preorder_reverse(root)
        # self.postorder_reverse(root)
        # self.levelorder_reverse(root)
        self.inorder_reverse(root)
        return root