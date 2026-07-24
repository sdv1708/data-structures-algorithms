class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vow = set('aeiou')
        prefix = [0] * (len(words) + 1)

        for ind, w in enumerate(words): 
            is_vowel = 1 if (w[0] in vow and w[-1] in vow) else 0 
            prefix[ind + 1] = prefix[ind] + is_vowel 

        return [prefix[r + 1] - prefix[l] for l, r in queries]