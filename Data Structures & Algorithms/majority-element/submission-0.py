class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        treshold = len(nums)/2
        freqMap = {} 
        for elt in nums:
            freqMap[elt] = freqMap.get(elt,0) + 1

        for k,v in freqMap.items() :
            if v > treshold:
                return k