class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        if len(nums) == 1 and nums[0] == target:
            return 0

        l, r = 0, len(nums)-1


        while l < r:
            mid = (l + r)//2
            print(mid)

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid

            if l == r and nums[l] == target:
                return l
        
        return -1
        