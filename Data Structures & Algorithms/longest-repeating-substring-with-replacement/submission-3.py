class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)
        maxLen = 0
        mostFreqChar = 0

        l, r = 0, 0

        while r < len(s):
            charFreq[s[r]] += 1
            # mostFreqChar = max(mostFreqChar, charFreq[s[r]])
            mostFreqChar = max(list(charFreq.values()))

            while r-l+1 - mostFreqChar > k:
                charFreq[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            
            r += 1

        return maxLen
