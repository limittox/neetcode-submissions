class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2):
        #     return False

        s1map = defaultdict(int)
        for char in s1:
            s1map[char] += 1
        
        s2map = defaultdict(int)
        
        for i in range(len(s1)-1):
            s2map[s2[i]] += 1
        
        i = 0
        for j in range(len(s1)-1, len(s2)):
            s2map[s2[j]] += 1
            checkedCharacters = 0
            # check equality of the hashmaps
            for s1Char in s1map.keys():
                if s2map[s1Char] == s1map[s1Char]:
                    checkedCharacters += 1
                else:
                    break
            
            if checkedCharacters == len(s1map):
                return True
            
            s2map[s2[i]] -= 1
            i += 1
        
        return False
