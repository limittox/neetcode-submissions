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
        
        return [num for freq,num in minHeap]