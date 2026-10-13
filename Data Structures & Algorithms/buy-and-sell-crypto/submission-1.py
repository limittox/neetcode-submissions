class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        if tomorrow price increased, then buy today
        sell if tomorrow price is lower
        -> Now tomorrow price is the new buy price

        buyPrice = nums[0]

        There needs to be a terminating if condition of size of list is <= 2
        
        maxProfit = 0

        for i in range(1, len(nums)):
            if num[i] < num[i-1] and num[i-1]-buyPrice > 0:
                maxProfit += num[i-1]-buyPrice
                buyPrice = nums[i]
        
        """

        i, j = 0, 1
        maxProfit = 0
        # priceMin = sys.maxsize
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            else:
                maxProfit = max(maxProfit, prices[j] - prices[i])
            
            j += 1
        return maxProfit  