class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            productOfRest = 1
            for j, otherNum in enumerate(nums):
                if i == j:
                    continue
                productOfRest *= otherNum
            res.append(productOfRest)
        return res