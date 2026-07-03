class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        forwardProduct = [1, 1, 2, 8]
        backwardProduct = [48, 24, 6, 8]
        res = [48, 24, 12, 8]
        """

        forwardPassProducts = [1 for _ in range(len(nums))]

        for i in range(1,len(nums)):
            forwardPassProducts[i] = nums[i-1]*forwardPassProducts[i-1]
        
        backwardPassProducts = [1 for _ in range(len(nums))]

        for i in range(len(nums)-2, -1, -1):
            backwardPassProducts[i] = nums[i+1]*backwardPassProducts[i+1]
        
        productButSelf = []
        for fpp, bpp in zip(forwardPassProducts, backwardPassProducts):
            productButSelf.append(fpp*bpp)
        
        return productButSelf