class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)
        maxLen = 0

        l, r = 0, 0

        while r < len(s):
            charFreq[s[r]] += 1

            if r-l+1 - max(charFreq.values()) > k:
                charFreq[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            
            r += 1

        return maxLen
