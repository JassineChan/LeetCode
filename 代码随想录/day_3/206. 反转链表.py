# 206. 反转链表
# https://leetcode.cn/problems/reverse-linked-list/
# https://programmercarl.com/0206.%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.html

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 原地翻转
        # pre, cur = None, head
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre

        # 头插法
        if head == None or head.next == None:
            return head
        virtual_node = ListNode(0, head)
        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = virtual_node.next
            virtual_node.next = tmp
        return virtual_node.next