# 513. 找树左下角的值
# https://leetcode.cn/problems/find-bottom-left-tree-value/
# https://programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def preorder(self, root, depth):
        if root is None:
            return
        if root.left is None and root.right is None:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = root.val
        self.preorder(root.left, depth + 1)
        self.preorder(root.right, depth + 1)
        return 

    def inorder(self, root, depth):
        if root is None:
            return 
        self.inorder(root.left, depth + 1)
        if root.left is None and root.right is None:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = root.val
        self.inorder(root.right, depth + 1)
        return 

    def postorder(self, root, depth):
        if root is None:
            return 
        self.postorder(root.left, depth + 1)
        self.postorder(root.right, depth + 1)
        if root.left is None and root.right is None:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = root.val
        return

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -1
        self.result = 0
        # self.preorder(root, 0)
        # self.inorder(root, 0)
        self.postorder(root, 0)
        return self.result
        # from collections import deque
        # queue = deque()
        # queue.append(root)
        # result = 0
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if i == 0:
        #             result = node.val
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return result