class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next, self.right.prev = self.right, self. left


    def remove(self, node) -> None:
        # remove node from DLL
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node) -> None:
        # insert at the rightmost end

        self.right.prev.next = node
        node.prev = self.right.prev

        self.right.prev = node
        node.next = self.right
    
    def get(self, key: int) -> int:
        # make it the most recent
        if key not in self.cache:
            return -1
        self.remove(self.cache[key]) # remove
        self.insert(self.cache[key]) # insert

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        # create node, add it to DLL, update cache (add, optionally remove the oldest)
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key]) # remove
            self.insert(self.cache[key]) # insert

        else:    
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

            if len(self.cache) > self.capacity:
                # delete the oldest
                key = self.left.next.key
                self.remove(self.left.next) # del form DLL

                del self.cache[key] # del from cache map

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)