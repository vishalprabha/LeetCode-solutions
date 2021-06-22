'''
Source: https://leetcode.com/problems/lru-cache/
Author: Vishal Prabhachandar
Date: 2021-June-22

Time complexity: O(1)
Space complexity: O(n)  
'''

# node structure
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    '''
        Implementing LRU Cache
    '''
    def __init__(self, capacity: int):
        '''
            Initializing the object

            :param  capacity: integer
        '''
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        '''
            Get the Key if present

            :param  key: integer
            :return value: integer
        '''
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1


    def put(self, key: int, value: int) -> None:
        '''
            Insert key, value in LRU Cache

            :param  key: integer
            :param  value: integer
            :return : None
        '''
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
            
    def _remove(self, node):
        '''
            Helper function to remove node

            :param  node: obj of class node
            :return : None
        '''
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        '''
            Helper function to add node

            :param  node: obj of class node
            :return : None
        '''
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)