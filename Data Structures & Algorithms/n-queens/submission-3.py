class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, anti, diag = set(), set(), set()

        board = [['.'] * n for _ in range(n)]
        result = []

        def backtrack(r): 
            if r == n: 
                result.append([''.join(row) for row in board])
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
        return result    