class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        hashset = set() 
        maxLen = 0 

        while r < len(s): 
            while s[r] in hashset: # shrink the window by removing s[l]
                hashset.remove(s[l])
                l += 1 
            
            hashset.add(s[r])
            maxLen = max(r - l + 1, maxLen)
            r += 1 
        
        return maxLen

        