class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0]) 
        maxArea = 0 

        def dfs(r, c): # the function is just to mark as visited
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0: 
                return 0 
            
            area = 1 
            grid[r][c] = 0
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            
            return area 
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea