class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def backtrack(curr_state: int) -> int:
            if curr_state == 0:
                return 1
            if curr_state in memo:
                return memo[curr_state]
            
            res = 0
            for c in [1, 2]:
                if curr_state < c:
                    continue
                
                res += backtrack(curr_state - c)
            memo[curr_state] = res
            return res
        
        return backtrack(n)