class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve(n:int)-> int:
            if n in memo:
                return memo[n]
            if n < 2:
                return 1
            res = solve(n-1) + solve(n-2)
            memo[n] = res 
            return res

        return solve(n)