class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numIndexMap = defaultdict(list)

        for i, num in enumerate(nums):
            numIndexMap[num].append(i)
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = -(nums[i]+nums[j])
                if numIndexMap[target]:
                    for index in numIndexMap[target]:
                        if index == i or index == j:
                            continue
                        triplet = tuple(sorted((nums[i], nums[j], target)))
                        # numIndexMap[target].remove(index)
                        res.add(triplet)
                        break
        return [list(triplet) for triplet in res]