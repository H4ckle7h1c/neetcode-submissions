class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Step 1 : Max heap
        heapq.heapify_max(stones)

        # Step 2: Simulation
        while len(stones) > 1:
            h1 = heapq.heappop_max(stones)
            h2 = heapq.heappop_max(stones)

            if h1 == h2:
                continue
            
            res = h1 - h2
            heapq.heappush_max(stones, res)

        if not stones:
            return 0
        
        return stones[0]




