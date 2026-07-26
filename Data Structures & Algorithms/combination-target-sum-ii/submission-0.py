class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        state = []
        res = []
        candidates.sort()

        def backtrack(start, total, state) -> None:
            if total == target:
                res.append(state.copy())
                return
            
            if total > target:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                state.append(candidates[i])
                backtrack(i+1, total + candidates[i], state)
                state.pop()

        backtrack(0, 0, [])
        return res