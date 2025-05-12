# 113. 路径总和 II
# https://leetcode.cn/problems/path-sum-ii/
# https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_search(self, root, ans, path, cur_target):
        path.append(root.val)
        if root.left == None and root.right == None and cur_target - root.val == 0:
            # 这里需要将路径“复制”到结果中
            # ans.append(path)
            ans.append(path[:])
        if root.left:
            self.preorder_search(root.left, ans, path, cur_target-root.val)
            path.pop()
        if root.right:
            self.preorder_search(root.right, ans, path, cur_target-root.val)
            path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        ans, path = [], []
        self.preorder_search(root, ans, path, targetSum)
        return ans