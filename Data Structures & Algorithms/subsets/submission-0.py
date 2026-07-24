class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, state) -> None:
            res.append(state.copy())

            for i in range(start,len(nums)):
                state.append(nums[i])
                backtrack(i+1, state)
                state.pop()
        backtrack(0, [])
        return res





