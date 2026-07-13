class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            maxTemp = Max Heap
            
        """
        res = [0] * len(temperatures)
        tempStack = []

        for i, temp in enumerate(temperatures):
            while tempStack and temp > tempStack[-1][0]:
                lowerTempPos = tempStack[-1][1]
                res[lowerTempPos] = i - lowerTempPos
                tempStack.pop()
            tempStack.append((temp, i))
        
        return res