class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [-1 for n in range(0,2*len(nums))]
        for n in range(0,len(nums)):
            ans[n] = nums[n]
            ans[n+len(nums)] = nums[n]

        return ans