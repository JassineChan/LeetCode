# 148. 排序链表
# https://leetcode.cn/problems/sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 自顶向下排序(左闭右开)
    def merge_sort_top_down(self, head, tail):
        # 空链表
        if head == None:
            return head
        # 单节点链表
        if head.next == tail:
            # 断开后面部分
            head.next = None
            return head
        # 快慢双指针寻找中间节点
        fast, slow = head, head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        # 递归排序与合并左右两边的链表
        return self.merge(self.merge_sort_top_down(head, slow), self.merge_sort_top_down(slow, tail))


    # 自底向上归并排序
    def merge_sort_bottom_up(self, head):
        # 空链表
        if head == None:
            return head
        # 单节点链表
        if head.next == None:
            return head
        # 链表长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # 虚拟头节点
        virtual_head = ListNode(0, head)
        # 子链表长度
        sub_length = 1
        # 判断排序是否完成
        while sub_length < length:
            pre, cur = virtual_head, virtual_head.next
            # 迭代归并相邻链表
            while cur:
                # 子链表1
                head1 = cur
                for i in range(sub_length-1):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                # 子链表2
                head2 = cur.next
                cur.next = None # 断开后面部分
                cur = head2
                for i in range(sub_length-1):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                # 记录下次循环开始位置
                next_start = None
                if cur:
                    next_start = cur.next
                    cur.next = None # 断开后面部分
                # 合并左右两边的链表
                merged = self.merge(head1, head2)
                pre.next = merged
                # 移动到合并链表尾节点
                while pre.next:
                    pre = pre.next
                cur = next_start
            sub_length *= 2
        return virtual_head.next


    # 合并两个有序链表
    def merge(self, head1, head2):
        virtual_head = ListNode(0)
        pre = virtual_head
        cur_1, cur_2 = head1, head2
        while cur_1 and cur_2:
            if cur_1.val <= cur_2.val:
                pre.next = cur_1
                pre = pre.next
                cur_1 = cur_1.next
            else:
                pre.next = cur_2
                pre = pre.next
                cur_2 = cur_2.next
        if cur_1:
            pre.next = cur_1
        elif cur_2:
            pre.next = cur_2
        return virtual_head.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # O(nlogn)时间复杂度
        # cur = head
        # values = []
        # while cur:
        #     values.append(cur.val)
        #     cur = cur.next
        # values = sorted(values)
        # virtual_head = ListNode(0, next=None)
        # pre = virtual_head
        # for i in range(len(values)):
        #     node = ListNode(values[i], next=None)
        #     pre.next = node
        #     pre = pre.next
        # return virtual_head.next

        # # 自顶向下归并排序
        # return self.merge_sort_top_down(head, None)
        
        # 自底向上归并排序
        return self.merge_sort_bottom_up(head)
        
        