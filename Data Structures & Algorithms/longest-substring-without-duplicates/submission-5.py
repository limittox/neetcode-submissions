class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()

        i, j = 0,0
        longestSub = 1

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(s[j])
            longestSub = max(len(seen), longestSub)
            j += 1
        
        return longestSub