class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        prod = 1
        
        # for i in range(n):
        #     if nums[i] != 0:
        #         prod = prod * nums[i]

        # for i,n in enumerate(nums):
        #     if n != 0:
        #         output[i] = int(prod/n)
        
        for i in range(n):
            prod = 1
            for j in range(n):
                if j == i:
                    continue 
                prod = prod * nums[j]
            output[i] = prod
        return output
            