from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)

        for i, letter in enumerate(s):
            count[letter] += 1
        
        for i, letter in enumerate(t):
            count[letter] -= 1
        
        for letter, value in count.items():
            if value != 0:
                return False
        
        return True
            

