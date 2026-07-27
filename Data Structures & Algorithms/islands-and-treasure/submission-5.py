class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647 

        queue = deque()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == 0: 
                    queue.append((r, c))
        
        while queue: 
            r, c = queue.popleft()
            for dr, dc in dirs: 
                nr, nc = r + dr, c + dc 
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != INF: 
                    continue 
                
                grid[nr][nc] = grid[r][c] + 1 
                queue.append((nr, nc))

        