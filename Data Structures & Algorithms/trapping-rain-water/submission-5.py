class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        water_area = 0
        prefix = [0] * len(height)  
        suffix = [0] * len(height)
        
        max_l = 0
        for i in range(n):
            max_l = max(max_l, height[i])
            prefix[i] = max_l

        max_r = 0
        for i in range(n - 1, -1, -1):
            max_r = max(max_r, height[i])
            suffix[i] = max_r

        for i in range(n):
            container_h = min(suffix[i], prefix[i])
            water_area += container_h - height[i]
        
        return water_area
                 


