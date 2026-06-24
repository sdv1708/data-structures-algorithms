class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        rows = len(grid)
        cols = len(grid[0])
        time = 0 

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = deque()

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2: 
                    queue.append((r, c)) 
        

        while queue and fresh > 0: 
            for _ in range(len(queue)): 
                r, c = queue.popleft()

                for dr, dc in dirs: 
                    nr, nc = r + dr, c + dc 
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1: 
                        grid[nr][nc] = 2 
                        fresh -= 1 
                        queue.append((nr, nc))
            
            time += 1 
        
        return time if fresh == 0 else -1

        