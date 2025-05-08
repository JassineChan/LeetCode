# 203. 移除链表元素
# https://leetcode.cn/problems/remove-linked-list-elements/
# https://programmercarl.com/0203.%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.html

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # # 虚拟头节点
        # virtual_head = ListNode(0, next=head)
        # pre = virtual_head
        # while pre.next:
        #     # 利用pre节点来删除当前节点
        #     if pre.next.val == val:
        #         pre.next = pre.next.next
        #     else:
        #         pre = pre.next
        # return virtual_head.next
        
        # 若不使用虚拟头节点，需要对头节点进行特殊处理
        while head and head.val == val:
            head = head.next
        if head == None:
            return
        pre = head
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head
