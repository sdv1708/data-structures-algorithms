class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c): # the function is just to mark as visited
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == '0': 
                return  
            
            grid[r][c] = '0'
            for dr, dc in dirs: 
                dfs(r + dr, c + dc)
        
        island = 0
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == '1': 
                    dfs(r, c)
                    island += 1 
        
        return island
        



        