class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Step 1: First find the row the target number is in
        Step 2: Execute binary search in that row

        Step 1:
        Use binary search on the first col
        Validate if the target number could be in that found row (i.e. matrix[i][0] <= target <= matrix[i][len(matrix[0])-1])
        
        We need to search through matrix[0][i]
        l, r = 0, len(matrix)

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        if target > matrix[0][r] and target > matrix[0][len(matrix[0])-1]:
            return False
        
        l, r = 0, len(matrix[0][r])
        """

        l, r = 0, len(matrix)-1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        if target > matrix[r][-1]:
            return False
        
        row = r

        l, r = 0, len(matrix[row])-1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        
        # l, r = 0, len(matrix[0][r])
        # return True