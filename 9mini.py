from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
cache = LRUCache(3)
for i in range(6):
    cache.put(i,i)
print(2 in cache.cache.values()) #False

    
    
    
