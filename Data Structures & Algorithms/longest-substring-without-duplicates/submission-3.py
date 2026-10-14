class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        uniqueElems = set()

        i, j = 0, 1

        uniqueElems.add(s[i])
        maxSubString = 1

        while j < len(s):
            if s[j] not in uniqueElems:
                # uniqueElems.add(s[j])
                maxSubString = max(maxSubString, len(uniqueElems)+1)
            else:
                while s[j] in uniqueElems:
                    uniqueElems.remove(s[i])
                    i += 1
            uniqueElems.add(s[j])
            j += 1

        return maxSubString
