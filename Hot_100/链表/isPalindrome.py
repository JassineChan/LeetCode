# 234. 回文链表
# https://leetcode.cn/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找中间节点
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # 反转链表的后半部分(头插法)
        pre, cur = slow, slow.next
        while cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        # 依次判断值是否相等
        right = slow.next
        left = head
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True