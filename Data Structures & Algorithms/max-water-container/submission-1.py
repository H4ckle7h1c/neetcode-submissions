class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            heigth = min(heights[l], heights[r])
            width = r - l
            area = max(area, heigth * width)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]: 
                r -= 1 

        return area