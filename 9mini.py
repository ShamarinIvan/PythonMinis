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

def fibonacci(n, cache=None):
    if cache is None:
        cache = LRUCache(10)
    
    if n <= 2:
        return 1
    if (result := cache.get(n)) is not None:
        return result
    result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    cache.put(n, result)
    return result

print(fibonacci(6))
        

    
    
