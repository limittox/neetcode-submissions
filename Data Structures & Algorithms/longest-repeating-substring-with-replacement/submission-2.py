class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        mostFreq = 0
        maxLen = 0
        l, r = 0, 0

        while r < len(s):
            char_freq[s[r]] += 1
            mostFreq = max(mostFreq, char_freq[s[r]])


            if (r-l+1) - mostFreq > k:
                char_freq[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r-l+1)
            r += 1
        
        return maxLen
