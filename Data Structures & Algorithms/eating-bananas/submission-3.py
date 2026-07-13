class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h - time constraint to eat bananas
        # k - eating rate
        # len(pile) < h => k [0,max(pile)]: si k=max(pile) -> h = len(pile)

        # t = sum(ceil(x/k) for x in piles)

        l, r = 1, max(piles)

        while l < r:
            k = (r+l) // 2
            
            t = sum(math.ceil(x/k) for x in piles)
            
            if t > h:
                l = k + 1
            else:
                r = k
        
        return r