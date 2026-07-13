class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, temp in enumerate(temperatures):
            if i == len(temperatures) - 1:
                res.append(0)
                break
            for j, futureTemp in enumerate(temperatures[i+1:]):
                if futureTemp > temp:
                    res.append(j+1)
                    break
                if j == len(temperatures[i+1:]) - 1:
                    res.append(0)

        return res