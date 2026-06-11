class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        # maintain the visited set for the indices instead of the numbers themselves
        def backtrack(path, visited): 
            if len(path) == len(nums): 
                result.append(list(path)) 
                return
            

            for i in range(len(nums)):
                if i in visited: 
                    continue 
                
                if i > 0 and nums[i] == nums[i-1] and (i - 1) not in visited:
                    continue
                
                visited.add(i)
                path.append(nums[i])
                backtrack(path, visited)
                visited.remove(i)
                path.pop()
        

        visited = set()
        backtrack([], visited)

        return result

        