# 707. 设计链表
# https://leetcode.cn/problems/design-linked-list/
# https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.virtual_head = ListNode(0, None)
        # 记录链表的长度可以避免通过遍历链表来判断index是否有效
        self.size = 0

    def get(self, index: int) -> int:
        if index > self.size-1:
            return -1
        pre = self.virtual_head
        while index > 0:
            pre = pre.next
            index -= 1
        return pre.next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        node = ListNode(val)
        pre = self.virtual_head
        while index > 0:
            pre = pre.next
            index -= 1
        node.next = pre.next
        pre.next = node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index > self.size-1:
            return
        pre = self.virtual_head
        while index > 0:
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)