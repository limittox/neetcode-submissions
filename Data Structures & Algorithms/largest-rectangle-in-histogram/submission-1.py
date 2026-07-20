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
        """

        """
        Optimal Solution
        """
        heights.append(0)

        indexOfHeightsTraversed = []
        maxArea = 0

        for i in range(len(heights)):
            currHeight = heights[i]

            # print(f"{indexOfLastHeight=}, {lastHeight=}, {currHeight=}, {indexOfHeightsTraversed=}, {maxArea=}")

            while indexOfHeightsTraversed and currHeight < heights[indexOfHeightsTraversed[-1]]:
                lastIndex = indexOfHeightsTraversed.pop()
                lastHeight = heights[lastIndex]

                if not indexOfHeightsTraversed:
                    width = i          # spans [0 .. i-1]
                else:
                    width = i - indexOfHeightsTraversed[-1] - 1

                currArea = width * lastHeight
                maxArea = max(maxArea, currArea)

                
            
            indexOfHeightsTraversed.append(i)

        return maxArea
