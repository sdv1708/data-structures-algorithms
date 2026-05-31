class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        freq_s1 = Counter(s1)
        freq_win = {}
        k = len(s1)
        l = 0
        
        for r in range(len(s2)):
            freq_win[s2[r]] = 1 + freq_win.get(s2[r], 0)
            
            # When window size exceeds k, shrink it from the left
            if (r - l + 1) > k:
                freq_win[s2[l]] -= 1
                if freq_win[s2[l]] == 0: #
                    del freq_win[s2[l]]
                l += 1
                
            if freq_win == freq_s1:
                return True
                
        return False