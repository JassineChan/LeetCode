# 2. 两数相加
# https://leetcode.cn/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        virtual_head = ListNode(0, next=None)
        pre = virtual_head
        cur_1, cur_2 = l1, l2
        carry = 0
        while cur_1 and cur_2:
            sum_val = cur_1.val + cur_2.val + carry
            carry = sum_val // 10
            val = sum_val % 10
            node = ListNode(val, next=None)
            pre.next = node
            pre = pre.next
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        while cur_1:
            sum_val = cur_1.val + carry
            carry = sum_val // 10
            val = sum_val % 10
            node = ListNode(val, next=None)
            pre.next = node
            pre = pre.next
            cur_1 = cur_1.next
        while cur_2:
            sum_val = cur_2.val + carry
            carry = sum_val // 10
            val = sum_val % 10
            node = ListNode(val, next=None)
            pre.next = node
            pre = pre.next
            cur_2 = cur_2.next
        if carry:
            node = ListNode(carry, next=None)
            pre.next = node
            pre = pre.next
        return virtual_head.next