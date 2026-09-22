class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        vote = 0
        
        for i in range(len(nums)):
            if vote == 0:
                candidate = nums[i]
                vote = 1
            elif nums[i] == candidate:
                vote += 1
            else:
                vote -= 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                count += 1

        if (count > len(nums)/2):
            return candidate

        return -1