class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numList = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numList:
                current = num
                length = 1

                while current + 1 in numList:
                    length += 1
                    current += 1
                if length > longest:
                    longest = length
            
        
        return longest
            