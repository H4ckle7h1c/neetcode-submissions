class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r,c) -> None:
            if visited.get((r,c)) or grid[r][c] == '0': 
                return 0
            
            visited[(r,c)]=True
            
            if r-1 >= 0:
                dfs(r-1,c)
            if r+1 < rows:
                dfs(r+1,c)
            if c-1 >= 0:
                dfs(r,c-1)
            if c+1 < cols:
                dfs(r,c+1)            
            
            return 1 

        for r in range(rows):
            for c in range(cols):
                if visited.get((r,c)): 
                    continue
                islands += dfs(r,c)
        
        return islands