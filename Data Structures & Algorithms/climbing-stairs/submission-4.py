class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def backtrack(curr_state: int) -> int:
            if curr_state == 0:
                return 1
            elif curr_state < 0:
                return 0
            elif curr_state in memo:
                return memo[curr_state]
            
            memo[curr_state] =  backtrack(curr_state - 1 ) + backtrack(curr_state - 2)
            return memo[curr_state]
        
        return backtrack(n)