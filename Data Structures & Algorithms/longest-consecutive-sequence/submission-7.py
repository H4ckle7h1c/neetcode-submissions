class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numList = set(nums)
        candidates = []
             
        if len(nums) == 0 :
            return 0

        for num in nums:
            if num - 1 not in numList and num + 1 in numList:
                candidates.append(num)
        
        if len(candidates) == 0:
            return 1
            
        longest = 1
        for c in candidates:
            chainPos = c  + 1
            currLength = 1
            while chainPos in numList:
                currLength += 1
                chainPos += 1
            if currLength > longest:
                longest = currLength
        
        return longest
            