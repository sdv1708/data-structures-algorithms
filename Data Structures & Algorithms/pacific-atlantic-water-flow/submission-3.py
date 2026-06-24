class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac = set()
        atl = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            if (r, c) not in visited: 
                visited.add((r, c)) 
            
            for dr, dc in dirs: 
                nr = r + dr 
                nc = c + dc 

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS: 
                    continue 
                
                if (nr, nc) in visited: 
                    continue 
                
                if heights[nr][nc] < heights[r][c]: 
                    continue 
            
                dfs(nr, nc,visited)
        

        # pacific top row 
        for c in range(COLS): 
            if (0, c) not in pac:
                dfs(0, c, pac)

        # pacific first col
        for r in range(ROWS): 
            if (r, 0) not in pac:
                dfs(r, 0, pac)
        
        # atlantic last col  
        for r in range(ROWS): 
            if (r, COLS - 1) not in atl:
                dfs(r, COLS - 1, atl)
        
        # atlantic bottom row
        for c in range(COLS): 
            if (ROWS - 1, c) not in atl:
                dfs(ROWS - 1, c, atl)
        
        output = []
        for r in range(ROWS): 
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl: 
                    output.append([r, c])
        
        return output

