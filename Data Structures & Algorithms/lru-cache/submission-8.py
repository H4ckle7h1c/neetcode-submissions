from typing import Optional

class Node:
    def __init__(self, key:int = 0, value: int = 0, next: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.value = value
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node) -> None:
        head_next = self.head.next 
        head_next.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = head_next

    def _remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]        
        self._remove(node)
        self._add_to_head(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if self.capacity == self.curr_size:
                lru = self.tail.prev
                self._remove(lru)
                self.cache.pop(lru.key)
                self.curr_size -= 1
            node = Node(key,value)
            self.cache[key] = node
            self._add_to_head(node)
            self.curr_size += 1

        
