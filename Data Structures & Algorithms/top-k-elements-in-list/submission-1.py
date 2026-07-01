class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = defaultdict(int)

        for num in nums:
            numFreq[num] += 1
        
        kMostFreqElems = []

        for num in numFreq.keys():
            if numFreq[num] >= k:
                kMostFreqElems.append(num)



        return sorted(numFreq, key=numFreq.get, reverse=True)[:k]