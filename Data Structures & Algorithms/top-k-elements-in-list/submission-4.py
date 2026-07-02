class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = defaultdict(int)

        for num in nums:
            numFreq[num] += 1
        
        minHeap = []

        for num, freq in numFreq.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = [num for freq,num in minHeap]
        # while len(minHeap) > 0:
        #     res.append(heapq.heappop(minHeap)[1])
        
        return res

        # return sorted(numFreq, key=numFreq.get, reverse=True)[:k]