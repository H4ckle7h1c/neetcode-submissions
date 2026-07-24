class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(state, start, total) -> None:
            if total == target:
                res.append(state.copy())
            
            if total > target:
                return 

            for i in range(start, len(nums)):
                state.append(nums[i])
                backtrack(state, i, total + nums[i])
                state.pop()

        backtrack([], 0, 0)
        return res
