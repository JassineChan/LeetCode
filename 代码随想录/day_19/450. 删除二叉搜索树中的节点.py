# 450. 删除二叉搜索树中的节点
# https://leetcode.cn/problems/delete-node-in-a-bst/
# https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 未找到目标节点
        if not root:
            return None
        # 已找到目标节点
        if root.val == key:
            # 如果节点的左右孩子均为空, 直接删除节点
            if not root.left and not root.right:
                return None
            # 如果节点的左孩子为空且右孩子非空, 返回右孩子
            elif not root.left and root.right:
                return root.right
            # 如果节点的左孩子非空且右孩子为空, 返回左孩子
            elif root.left and not root.right:
                return root.left
            # 如果节点的左右孩子均非空, 将左孩子作为右孩子最左子节点的左孩子
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                # 1. 直接把左子树接到最左节点下方，容易破坏平衡
                # cur.left = root.left
                # return root.right
                # 2. 将中序后继的值赋给当前节点，然后递归删除中序后继节点
                # 这样既保留了BST的结构，又不会增加树的高度
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
                return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root 