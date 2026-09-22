class Solution:
    def trap(self, height: List[int]) -> int:
        water_area = 0
        max_l, max_r = 0, 0
        prefix = [0] * len(height)  
        suffix = [0] * len(height)
        
        for i in range(len(height)):
            max_l = max(max_l, height[i])
            prefix[i] = max_l

        for i in range(len(height) - 1, -1, -1):
            max_r = max(max_r, height[i])
            suffix[i] = max_r
        print(suffix, prefix)

        for i in range(len(height)):
            container_h = min(suffix[i], prefix[i])
            water_area += container_h - height[i]
        
        return water_area
                 


