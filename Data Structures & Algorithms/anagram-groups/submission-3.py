class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)

        """
        go through every word, convert them to a tuple of freqs
            - Assuming tha tall the letters are lowercase
        
        then add those tuples to wordDict

        then return the wordDict values as a list

        """

        for word in strs:
            letterFreq = [0 for _ in range(26)]
            for letter in word:
                letterFreq[ord(letter)-ord('a')] += 1
            
            tupleLetterFreq = tuple(letterFreq)

            wordDict[tupleLetterFreq].append(word)
        
        return list(wordDict.values())