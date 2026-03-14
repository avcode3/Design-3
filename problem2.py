# problem 2

# https://leetcode.com/problems/lru-cache/

class LRUCache:

    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val 
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1 
        node = self.map[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.val


    # always keep (-1,-1) as the last node
    def removeNode(self,node):
        node.prev.next = node.next 
        node.next.prev = node.prev 
        node.prev = None 
        node.next = None

    # always keep (-1,-1) as the head node
    def addToHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node 
        self.head.next = node

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if len(self.map) == self.capacity:
                last_node = self.tail.prev
                self.removeNode(last_node) # remove the last node 
                del self.map[last_node.key]
            new_node = self.Node(key,value)
            self.addToHead(new_node)
            self.map[key] = new_node
        else:
            old_node = self.map[key]
            old_node.val = value
            self.removeNode(old_node)
            self.addToHead(old_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)