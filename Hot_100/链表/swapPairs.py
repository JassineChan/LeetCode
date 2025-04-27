# 24. 两两交换链表中的节点
# https://leetcode.cn/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        virtual_head = ListNode(0, next=head)
        pre, cur = virtual_head, virtual_head.next
        while cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            pre.next = tmp
            # cur只需走一步
            cur = cur.next
            # pre需要走两步 
            pre = pre.next.next
        return virtual_head.next