class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs: 
            freq = [0] * 26 
            for c in word: 
                freq[ord(c) - ord('a')] += 1 
            group[tuple(freq)].append(word)
        
        return list(group.values())

        