class MyHashSet:

    def __init__(self):      
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        h = int(key) % self.size
        self.buckets[h] = key

    def remove(self, key: int) -> None:
        h = int(key) % self.size
        self.buckets[h] = 0

    def contains(self, key: int) -> bool:
        return key in self.buckets
        
        


# Your MyHashSet object will be instantiated and called as such:
key = '4'
obj = MyHashSet()
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)