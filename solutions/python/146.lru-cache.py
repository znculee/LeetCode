# 146. LRU Cache

class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.length = 0
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.map.keys():
            node = self.map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.dummy_head.next
            node.prev = self.dummy_head
            self.dummy_head.next.prev = node
            self.dummy_head.next = node
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            node = self.map[key]
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.dummy_head.next
            node.prev = self.dummy_head
            self.dummy_head.next.prev = node
            self.dummy_head.next = node
        else:
            node = Node(key, value, self.dummy_head, self.dummy_head.next)
            self.dummy_head.next.prev = node
            self.dummy_head.next = node
            self.map[key] = node
            self.length += 1
        if self.length > self.capacity:
            self.map.pop(self.dummy_tail.prev.key)
            self.dummy_tail.prev.prev.next = self.dummy_tail
            self.dummy_tail.prev = self.dummy_tail.prev.prev
            self.length -= 1

    def show(self) -> None:
        cur = self.dummy_head.next
        while cur.next:
            print(f'({cur.key}, {cur.value})', end='')
            cur = cur.next
            if cur.next:
                print(' -> ', end='')
            else:
                print('', end='\n')


def test():
    print('Create LRUCache')
    cache = LRUCache(2)
    cache.show()
    print('put(1, 1)', end=':\t')
    cache.put(1, 1)
    cache.show()
    print('put(2, 2)', end=':\t')
    cache.put(2, 2)
    cache.show()
    print('get(1)', end=':\t')
    print(cache.get(1), end='\t')
    cache.show()
    print('put(3, 3)', end=':\t')
    cache.put(3, 3)
    cache.show()
    print('put(4, 4)', end=':\t')
    cache.put(4, 4)
    cache.show()
    print('get(1)', end=':\t')
    print(cache.get(1), end='\t')
    cache.show()
    print('get(3)', end=':\t')
    print(cache.get(3), end='\t')
    cache.show()
    print('get(4)', end=':\t')
    print(cache.get(4), end='\t')
    cache.show()
    print('put(3, 7)', end=':\t')
    cache.put(3, 7)
    cache.show()
    print('get(3)', end=':\t')
    print(cache.get(3), end='\t')
    cache.show()


if __name__ == '__main__':
    test()
