class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for par in s:
            if par in '({[':
                stack.append(par)
            else:
                # Check if stack is empty before popping or if brackets don't match
                if not stack or stack[-1] != map[par]:
                    return False
                stack.pop()
        
        return not stack