class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Prefix
        output = [1] * n
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]

        # Final answer
        postfix = 1;
        for i in range(n-1,-1,-1):
            output[i] = output[i] * postfix
            postfix = nums[i] * postfix
            

        return output
            