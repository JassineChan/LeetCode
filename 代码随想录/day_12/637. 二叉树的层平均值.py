# 637. 二叉树的层平均值
# https://leetcode.cn/problems/average-of-levels-in-binary-tree/
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 层序遍历
        from collections import deque
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            count = 0
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.popleft()
                count += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(count/q_len)
        return ans
            