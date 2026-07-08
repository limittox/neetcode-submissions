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
            currConsecutiveNums = 1
            if num in seen:
                continue
            i = 1
            while num + i in numSet and num + i not in seen and num + i <= maxInNums:
                seen.add(num+i)
                currConsecutiveNums += 1
                i += 1
            if num + i in seen:
                currConsecutiveNums += seenCount[num+i]
            seenCount[num] = currConsecutiveNums
            maxConsecutiveNums = max(maxConsecutiveNums, currConsecutiveNums)

            seen.add(num)
        return maxConsecutiveNums