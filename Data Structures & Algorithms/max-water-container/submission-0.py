class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i, hi in enumerate(heights):
            for j in range(i+1,len(heights)):
                h =  min(hi,heights[j])
                l = j - i 
                area = max(area, l*h)

        return area