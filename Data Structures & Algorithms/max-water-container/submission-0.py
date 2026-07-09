class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Area calc = (r-l)*heightOfShortestBar
        [1,2,3,4,5,6]
        l=0 and r=5, A=5
        l=1 and r=5, A=8
        l=2 and r=5, A=9
        l=3 and r=5, A=8
        l=4 and r=5, A=5

        [6,5,4,3,2,1] => Symmetry

        [1,1,1,1,1] -> move both bars

        [1,2,3,2,1]
        """

        l, r = 0, len(heights)-1
        maxArea = 0
        while l < r:
            area = (r-l)*min(heights[l], heights[r])
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
                r -= 1
        
        return maxArea