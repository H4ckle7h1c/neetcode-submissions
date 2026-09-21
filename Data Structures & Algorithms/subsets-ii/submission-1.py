class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        seen = {}
        nums.sort()
        def backtrack(state: Optional[List[int]]) -> None:
            current_state = tuple(curr)
            if current_state not in seen:
                res.append(curr.copy())
                seen[current_state] = True

            for i in range(0,len(state)):
                curr.append(state[i])
                backtrack(state[i+1::])
                curr.pop()

        
        backtrack(nums)
        return res

            
