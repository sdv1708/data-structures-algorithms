class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0 : 1}
        res = 0 
        prefixSum = 0 

        for num in nums: 
            prefixSum += num

            diff = prefixSum - k
            if (diff) in prefix_count:
                res += prefix_count[diff]

            prefix_count[prefixSum] = 1 + prefix_count.get(prefixSum, 0)

        return res
                    