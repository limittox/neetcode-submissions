class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = defaultdict(int)
        windowmap = defaultdict(int)
        formed = 0
        shortestSub = -1

        for c in t:
            tmap[c] += 1
        
        l, r = 0, 0

        while r < len(s):
            windowmap[s[r]] += 1

            if s[r] in tmap and windowmap[s[r]] == tmap[s[r]]:
                formed += 1
            
            while formed == len(tmap):
                if shortestSub == -1 or len(shortestSub) > r-l+1:
                    shortestSub = s[l:r+1]
                windowmap[s[l]] -= 1

                if s[l] in tmap and windowmap[s[l]] < tmap[s[l]]:
                    formed -= 1
                l += 1
            
            r += 1
        
        return shortestSub if shortestSub != -1 else ""