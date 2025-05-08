# 199. 二叉树的右视图
# https://leetcode.cn/problems/binary-tree-right-side-view/
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        # 层序遍历找每层的最后一个节点
        from collections import deque
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                if i == queue_len - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans