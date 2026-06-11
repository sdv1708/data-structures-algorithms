class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(c_open, c_close, path): 
            if c_open + c_close == 2 * n: 
                result.append("".join(list(path)))
                return 
                
            if c_open < n: 
                path.append('(')
                c_open += 1 
                backtrack(c_open, c_close, path)
                c_open -= 1 
                path.pop()
            
            if c_close < c_open: 
                path.append(')')
                c_close += 1
                backtrack(c_open, c_close, path)
                c_close -= 1 
                path.pop()
        
        backtrack(0, 0, [])
        return result
