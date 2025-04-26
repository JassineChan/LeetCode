# 160. 相交链表
# https://leetcode.cn/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_len, b_len = 0, 0
        a_cur = headA
        while a_cur:
            a_len += 1
            a_cur = a_cur.next
        b_cur = headB
        while b_cur:
            b_len += 1
            b_cur = b_cur.next
        if a_len >= b_len:
            forward = a_len - b_len
            a_cur = headA
            for _ in range(forward):
                a_cur = a_cur.next
            b_cur = headB
            while a_cur and b_cur:
                if a_cur == b_cur:
                    return a_cur
                a_cur = a_cur.next
                b_cur = b_cur.next
        else:
            forward = b_len - a_len
            b_cur = headB
            for _ in range(forward):
                b_cur = b_cur.next
            a_cur = headA
            while a_cur and b_cur:
                if a_cur == b_cur:
                    return a_cur
                a_cur = a_cur.next
                b_cur = b_cur.next
        return None