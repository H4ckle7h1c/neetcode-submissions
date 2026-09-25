class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob1, rob2 = 0, 0
        
        for i in range(n-1, -1, -1):
            tmp = max(nums[i]+rob1, rob2)
            rob1, rob2 = rob2, tmp
        
        return rob2