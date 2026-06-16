class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, anti, diag = set(), set(), set()

        board = [['.'] * n for _ in range(n)]
        count = 0 

        def backtrack(r): 
            if r == n: 
                nonlocal count
                count += 1 
                return 

            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti:
                    continue 
                
                board[r][c] = 'Q'
                cols.add(c)
                anti.add(r + c)
                diag.add(r - c)
                
                backtrack(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                anti.remove(r + c)
                diag.remove(r - c)
            
        backtrack(0)
        return count    