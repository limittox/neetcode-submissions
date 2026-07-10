class Solution:
    def trap(self, height: List[int]) -> int:
        """
        totalWaterRet = 0
        currTallestBar = 0
        currWaterRet += height of currTallestBar - height of curr bar
        if we reach a bar that is taller or equal to currTallestBar:
            totalWaterRet += currTallestBar
            currTallestBar = new taller bar
            currWaterRet = 0

        """

        """
        []
        [0,2,0,1,1,0,1,3,2,1]: tick

        [4,3,2,3,0]: cross
        """

        if len(height) <= 2:
            return 0
        
        totalWaterRet = 0
        maxL, maxR = height[0], height[-1]

        l, r = 0, len(height)-1
        i = 0
        while l <= r:
            currWaterRet = min(maxL, maxR)-height[i]
            if currWaterRet > 0:
                totalWaterRet += currWaterRet
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if height[l] <= height[r]:
                l += 1
                i = l
            else:
                r -= 1
                i = r
        
        return totalWaterRet
            
