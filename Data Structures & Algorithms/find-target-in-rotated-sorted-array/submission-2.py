class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        case 1: Rotated and target is min
        case 2: Rotated and target is max
        case 3: Non-rotated and target is min
        case 4: Non-rotated and target is max
        case 5: Rotated and target is greater than mid
        case 6: Rotated and target is less than mid
        case 7: Non-rotated and target is greater than mid
        case 8: Non-rotated and target is less than mid
        case 9: Rotated and target is mid
        case 10: Non-rotated and target is mid 
        case 11: nums size is 1
        case 12: nums size is 2

        case 6:
        [3,4,5,6,1,2], target = 1
        l, r = 0, len(nums)-1 == 5
        mid = (0+5)//2 == 2
        nums[mid i.e. 2] == 5
        and the target is 1
            which is less than 5 i.e. mid
            check if nums[mid] is target, then return the index
            if mid is greater than num[l] it means the pivot isn't there
            AND if target is less than num[mid] it means it should be on the right side
                else: we need to search left side
            else means pivot is on the left side
            AND if the target is less than num[mid] means it should be on the left side
                else: we need to search right side
        
        
        
        While we are looking at the element @ mid
        ------------------------------------------
        [1,2,3,4,5,6] r6
        [3,4,5,6,1,2] r4
        [2,3,4,5,6,1] r5
        [6,1,2,3,4,5] r1
        
        if target > mid and l > r and target > r
            go left
        if target > mid and l < r and target > r
        

        How do we determine, which side the pivot is in:
            Base case: NO PIVOT: Set pivot point to the last element?
            compare nums[lo] with nums[hi]
            
        """
        # [5,1,3], target = 5
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r)//2
            print(f'{mid=}')
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[l] and target < nums[mid] and target >= nums[l]:
                r = mid - 1
            elif nums[mid] < nums[l] and (target < nums[mid] or target >= nums[l]):
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
