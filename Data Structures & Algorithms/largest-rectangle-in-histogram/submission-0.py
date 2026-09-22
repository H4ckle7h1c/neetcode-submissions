class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            minHeight = heights[i]
            for right in range(i, n):
                minHeight = min(minHeight, heights[right])
                width = right - i + 1
                max_area = max(max_area, minHeight * width)

        return max_area