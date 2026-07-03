class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = []
        for string in strs:
            encodedString.append(str(len(string)))
            encodedString.append("#")
            encodedString.append(string)
        # print(encodedString)
        return "".join(encodedString)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            k = i
            while s[k] != "#" and k < len(s):
                k += 1
            
            lengthOfString = s[i:k]
            digitLength = len(lengthOfString)
            lengthOfString = int(lengthOfString)

            start = i + digitLength + 1
            end = i + digitLength + lengthOfString + 1

            res.append(s[start:end])

            i = end
        
        return res