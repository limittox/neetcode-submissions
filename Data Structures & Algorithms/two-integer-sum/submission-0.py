from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)
        for i, num in enumerate(nums):
            count[target-num] = i
        
        for i, num in enumerate(nums):
            if count[num] and count[num] != i:
                return [i, count[num]]
        
        return [0,0]