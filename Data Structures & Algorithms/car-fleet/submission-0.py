class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
            0th car - 3 hours
            1st car - 4.5 hours
            2nd car - 10 hours
            3rd car - 3 hours

            sort them by pos
            0th car - 3 hours
            1st car - 3 hours
            2nd car - 4.5 hours
            3rd car - 10 hours

            pos = [0,1,6,7]
            spe = [1,1,4,2]

            0th car - 10 hours
            1st car - 9 hours
            2nd car - 1.5 hours
            3rd car - 1.5 hours
        """

        posAndSpeed = []

        for pos, speed in zip(position, speed):
            posAndSpeed.append((pos, speed))
        
        posAndSpeed.sort()

        
        timeTilTarget = []

        for pos, speed in posAndSpeed:
            timeUntilTargetIsReached = (target-pos)/speed
            timeTilTarget.append(timeUntilTargetIsReached)
        
        for i in range(len(timeTilTarget), -1, -1):
            if i+1 >= len(timeTilTarget):
                continue
            if timeTilTarget[i] < timeTilTarget[i+1]:
                timeTilTarget[i] = timeTilTarget[i+1]
        
        return len(set(timeTilTarget))