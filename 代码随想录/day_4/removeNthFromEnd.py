# 19. 删除链表的倒数第 N 个结点
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针
        virtual_head = ListNode(0, next=head)
        fast = virtual_head
        # fast先走n步
        for _ in range(n):
            fast = fast.next
        slow = virtual_head
        # slow和fast同步走
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return virtual_head.next