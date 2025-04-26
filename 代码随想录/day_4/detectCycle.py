# 142. 环形链表 II
# https://leetcode.cn/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针判断是否有环
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 链表有环，寻找入口点
            if fast == slow:
                # 从头结点出发一个指针，从相遇节点也出发一个指针
                # 这两个指针每次只走一步，那么这两个指针会在环形入口的节点相遇
                ans = head
                while ans != slow:
                    ans = ans.next
                    slow = slow.next
                return ans
        return None