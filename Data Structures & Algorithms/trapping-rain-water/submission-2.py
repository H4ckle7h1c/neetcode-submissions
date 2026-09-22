class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r = 0, len(height) - 1
        # max_l, max_r = 0,0 
        water_area = 0
        
        for i in range (0, len(height) - 1):
            max_l, max_r = 0,0 
            l,r = i-1,i+1
            
            # Discovery of the max in the left bound
            while l >= 0:
                max_l = max(max_l, height[l])
                l -= 1
            
            # Discovery of the max in the right bound
            while r <= len(height) - 1:
                max_r = max(max_r, height[r])
                r += 1

            water_area += max(min(max_r, max_l) - height[i],0)
        
        return water_area
                 


