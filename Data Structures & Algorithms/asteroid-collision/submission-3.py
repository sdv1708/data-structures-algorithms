class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids: 
            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] < abs(ast): 
                    stack.pop()
                    continue # check if there are other elements in the stack 
                    #  continue basically ignores the code below as long as the if condition is valid
                
                elif stack[-1] == abs(ast):
                    stack.pop()
                    break # both the incoming and the top asteroid is destroyed 
                
                else: 
                    break # incoming asteroid is smaller, so no use just break 
                
            else: 
                stack.append(ast)
        
        return stack

            





        