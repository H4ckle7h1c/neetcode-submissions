class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = nums
        self.capacity = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.capacity:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
