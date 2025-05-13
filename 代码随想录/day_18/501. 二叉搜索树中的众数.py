# 501. 二叉搜索树中的众数
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/
# https://programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if root.val == self.cur_num:
            self.cur_count += 1
        else:
            self.cur_num = root.val
            self.cur_count = 1
        if self.cur_count == self.max_count:
            self.ans.append(self.cur_num)
        elif self.cur_count > self.max_count:
            while self.ans:
                self.ans.pop()
            self.ans.append(self.cur_num)
            self.max_count = self.cur_count
        self.inorder(root.right)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # # 迭代中序遍历
        # ans, stack = [], []
        # cur_num, cur_count, max_count = None, None, 0
        # cur = root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     if cur.val == cur_num:
        #         cur_count += 1
        #     else:
        #         cur_num = cur.val
        #         cur_count = 1
        #     if cur_count == max_count:
        #         ans.append(cur_num)
        #     elif cur_count > max_count:
        #         while ans:
        #             ans.pop()
        #         ans.append(cur_num)
        #         max_count = cur_count
        #     cur = cur.right
        # return ans

        # 递归法
        self.ans = []
        self.cur_num, self.cur_count, self.max_count = None, None, 0
        self.inorder(root)
        return self.ans