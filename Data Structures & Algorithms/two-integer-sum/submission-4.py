class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        result = None
        for i, n in enumerate(nums):
            hashMap[n] = i 
        
        for i, num in enumerate(nums): 
            diff = target - num 

            if diff in hashMap and hashMap[diff] != i: 
                return [i, hashMap[diff]]
        
        return []
            



        