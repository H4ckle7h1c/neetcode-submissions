class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r,c) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or visited.get((r,c)):
                return 0

            visited[(r,c)]=True         
            
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)        
        
        area = 0 
        for r in range(rows):
            for c in range(cols):
                if visited.get((r,c)): 
                    continue
                area = max(area, dfs(r,c))
        
        return area