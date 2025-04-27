# 146. LRU 缓存
# https://leetcode.cn/problems/lru-cache/


# class LRUCache(collections.OrderedDict):

#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity


#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)

# 双向链表节点
class DLinkedNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


# 哈希表 + 双向链表
class LRUCache:
    def __init__(self, capacity: int):
        # key-address映射
        self.key2address = dict()
        # 虚拟头节点
        self.virtual_head = DLinkedNode(0, 0)
        # 虚拟尾节点
        self.virtual_tail = DLinkedNode(0, 0)
        # 连接头节点
        self.virtual_head.next = self.virtual_tail
        self.virtual_tail.prev = self.virtual_head
        # 链表容量
        self.capacity = capacity
        # 链表长度
        self.size = 0

    def get(self, key: int) -> int:
        # 如果key在链表中
        if key in self.key2address:
            node = self.key2address[key]
            value = node.value
            # 将节点移动到链表头部
            self.moveToHead(node)
            return value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        # 如果key在链表中
        if key in self.key2address:
            node = self.key2address[key]
            node.value = value
            # 将节点移动到链表头部
            self.moveToHead(node)
        else:
            node = DLinkedNode(key, value)
            # 添加key-address映射
            self.key2address[key] = node
            # 将节点插入到链表头部
            self.addToHead(node)
            self.size += 1
            # 如果链表长度超过容量, 移除链表尾部节点
            if self.size > self.capacity:
                node = self.virtual_tail.prev
                self.removeNode(node)
                self.size -= 1

    def moveToHead(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.virtual_head.next.prev = node
        node.next = self.virtual_head.next
        self.virtual_head.next = node
        node.prev = self.virtual_head

    def addToHead(self, node):
        self.virtual_head.next.prev = node
        node.next = self.virtual_head.next
        self.virtual_head.next = node
        node.prev = self.virtual_head

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.key2address.pop(node.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
