class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        seen = set()
        seenCount = defaultdict(int)
        maxInNums = max(nums)
        
        maxConsecutiveNums = 0
        for num in nums:
            if num-1 in numSet:
                continue
            i = 1
            while num + i in numSet:
                i += 1
            maxConsecutiveNums = max(maxConsecutiveNums, i)
        return maxConsecutiveNums