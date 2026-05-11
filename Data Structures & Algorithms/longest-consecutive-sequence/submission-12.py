class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        longest = 1 
        numSet = set(nums)

        for num in nums: 
            if (num - 1) not in numSet: 
                length = 1 
                while (num + length) in numSet: 
                    length += 1 
                    longest = max(length, longest)
        
        return longest

        