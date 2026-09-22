class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Prefix
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)

        # Final answer
        output = [0] * n
        postfix = 1;
        for i in range(n-1,-1,-1):
            output[i] = prefix[i] * postfix
            postfix = nums[i] * postfix
            

        return output
            