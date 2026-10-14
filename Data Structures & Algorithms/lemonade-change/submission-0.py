class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5, c10 = 0, 0 

        for bill in bills: 
            if bill == 5: 
                c5 += 1 

            elif bill == 10: 
                c10 += 1 
                if c5 >= 1: 
                    c5 -= 1
                else: 
                    return False 

            else: 
                change = bill - 5 
                if change == 15 and c5 > 0 and c10 > 0: 
                    c5 -= 1 
                    c10 -= 1 

                elif change == 15 and c5 >= 3: 
                    c5 -= 3 
                else: 
                    return False 

        return True  

        