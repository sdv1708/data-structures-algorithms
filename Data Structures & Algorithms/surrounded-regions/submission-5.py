class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c): 
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O' :
                return 
            
            board[r][c] = 'S'

            for dr, dc in dirs: 
                nr, nc = r + dr, c + dc 
                
                dfs(nr, nc)
        

        # marking all border 'O' as safe
        for r in range(ROWS): 
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1]): 
                    dfs(r, c)
            
            # making all internal O as X
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == 'O':
                    board[r][c] = 'X'

            # making all the border 'safe' marked grids as O
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == 'S':
                    board[r][c] = 'O'    
            



            



         