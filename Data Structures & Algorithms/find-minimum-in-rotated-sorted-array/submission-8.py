class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,6,1,2]
        [5,6,1,2,3,4]

        we have l and r pointers, find the mid
        if nums at l and nums at r are both greater than nums at mid -> mid is at min and we return that
        else we go towards min(nums[l] && nums[r])
            so if nums[l] < nums[r] 
                then r = mid or should it be r-1???
            else 
                l = mid
        
        """

        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]