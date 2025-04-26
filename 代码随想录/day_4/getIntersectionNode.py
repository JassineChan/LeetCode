# 面试题 02.07. 链表相交
# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 相交意味着后半段相同，所以要让后半段对齐
        a_len, b_len = 0, 0
        cur = headA
        while cur:
            a_len += 1
            cur = cur.next
        cur = headB
        while cur:
            b_len += 1
            cur = cur.next
        if a_len >= b_len:
            # 对齐
            forward = a_len - b_len
            a_cur = headA
            for i in range(forward):
                a_cur = a_cur.next
            b_cur = headB
            while a_cur and b_cur:
                if a_cur == b_cur:
                    return a_cur
                a_cur = a_cur.next
                b_cur = b_cur.next
        else:
            # 对齐
            forward = b_len - a_len
            b_cur = headB
            for i in range(forward):
                b_cur = b_cur.next
            a_cur = headA
            while a_cur and b_cur:
                if a_cur == b_cur:
                    return a_cur
                a_cur = a_cur.next
                b_cur = b_cur.next
        return None