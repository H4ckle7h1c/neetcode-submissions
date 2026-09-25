class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i < 2:
                continue
            nums[i] += max(nums[i-2], nums[i-3] if i >= 3 else 0)
        
        return max(nums[n-1], nums[n-2])