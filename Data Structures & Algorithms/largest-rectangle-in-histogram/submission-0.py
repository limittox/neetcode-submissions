class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        6*1 = 6
        2*2 = 4

        x   x
        x   x
        x   x
        x   x     x
        x   x     x
        x   x x x x
        x x x x x x

        x   x
        x   x
        x   x
        x   x     
        x   x     
        x   x      
        x x x x x x x x
        """

        """
        Brute force solution
        """
        maxArea = 0

        for i in range(len(heights)):
            currMaxArea = heights[i]
            for l in range(i-1, -1, -1):
                if heights[l] < heights[i]:
                    break
                currMaxArea += heights[i]
            
            for r in range(i+1, len(heights)):
                if heights[r] < heights[i]:
                    break
                currMaxArea += heights[i]
            
            maxArea = max(maxArea, currMaxArea)
        
        return maxArea