# 138. 随机链表的复制
# https://leetcode.cn/problems/copy-list-with-random-pointer/


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # virtual_head = Node(0, next=None, random=None)
        # pre = virtual_head
        # cur = head
        # # 旧节点地址到索引的映射
        # pos2idx = {}
        # # 新节点地址
        # pos_copy = []
        # index = 0
        # while cur:
        #     node = Node(cur.val, None, None)
        #     pos_copy.append(node)
        #     pre.next = node
        #     pre = pre.next
        #     pos2idx[cur] = index
        #     index += 1
        #     cur = cur.next
        # # 处理各节点的random域
        # cur = head
        # cur_copy = virtual_head.next
        # while cur:
        #     if cur.random:
        #         cur_copy.random = pos_copy[pos2idx[cur.random]]
        #     cur = cur.next
        #     cur_copy = cur_copy.next
        # return virtual_head.next


        # O(1)空间复杂度
        if not head:
            return None
        # 第一步：复制每个节点并插入到原节点之后
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        # 第二步：设置新节点的random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next  # 新节点的random指向原节点random的下一个
            # 如果cur.random为None，默认新节点的random也是None，无需操作
            cur = cur.next.next
        # 第三步：分离新旧链表
        new_head = head.next
        old_cur = head
        new_cur = new_head
        while old_cur:
            # 恢复原链表的next指针
            old_next = old_cur.next.next
            # 设置新链表的next指针
            if old_next:
                new_cur.next = old_next.next
            else:
                new_cur.next = None
            # 移动指针
            old_cur.next = old_next
            old_cur = old_next
            new_cur = new_cur.next
        return new_head