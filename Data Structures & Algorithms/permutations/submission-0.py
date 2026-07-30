class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = [False] * len(nums)

        def backtrack(state: List[int]) -> None:
            
            if len(state) == len(nums):
                res.append(state.copy())
                return

            for i, c in enumerate(nums):
                if chosen[i]:
                    continue 
                chosen[i] = True
                state.append(c)                
                backtrack(state)
                chosen[i] = False
                state.pop()

        backtrack([])

        return res