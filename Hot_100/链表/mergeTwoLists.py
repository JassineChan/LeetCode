# 21. 合并两个有序链表
# https://leetcode.cn/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        virtual_head = ListNode(0, next=None)
        cur = virtual_head
        cur_1, cur_2 = list1, list2
        while cur_1 and cur_2:
            if cur_1.val <= cur_2.val:
                cur.next = cur_1
                cur = cur.next
                cur_1 = cur_1.next
            else:
                cur.next = cur_2
                cur = cur.next
                cur_2 = cur_2.next
        if cur_1:
            cur.next = cur_1
        if cur_2:
            cur.next = cur_2
        return virtual_head.next