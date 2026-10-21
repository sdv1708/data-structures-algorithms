class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        time = 0 
        remaining = 0 
        queue = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    remaining += 1 # fresh count 

                if grid[r][c] == 2: 
                    queue.append((r, c)) # append all rotten ones 

        while queue and remaining > 0: 
            for _ in range(len(queue)): 
                r, c = queue.popleft() 

                for dr, dc in dirs: 
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1: 
                        grid[nr][nc] = 2 
                        remaining -= 1 
                        queue.append((nr, nc))
            time += 1 
        
        if remaining == 0: 
            return time 
        
        else: 
            return -1