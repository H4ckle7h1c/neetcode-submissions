class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = (r - l) // 2 + l 
            curr_t = sum(math.ceil(x/k) for x in piles)

            if curr_t > h:
                l = k+1
            elif curr_t <= h: 
                r = k-1
                res = k

        return res




        #0,1,2,3,4