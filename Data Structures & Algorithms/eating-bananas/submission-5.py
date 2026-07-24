class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles=[10,1,1,1], h = 5
        

        piles=[1,2,3,4]


        if h == len(piles):
            k = max(piles)

        Brute force:
        -----------
        go through nums between incl. len(piles) to h
            then return ans
        
        
        """
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile/mid)

            if hours_needed <= h:
                right = mid
            else:
                left = mid+1

        return left