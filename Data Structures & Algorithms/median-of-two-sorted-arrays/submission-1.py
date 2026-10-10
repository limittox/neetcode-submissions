class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A
        n, m = len(A), len(B)
        total = n + m
        half = total // 2

        left, right = 0, n

        POS_INF, NEG_INF = math.inf, -math.inf

        while True:
            i = (left + right) // 2
            j = half - i

            Aleft = A[i-1] if i > 0 else NEG_INF
            Aright = A[i] if i < n else POS_INF
            Bleft = B[j-1] if j > 0 else NEG_INF
            Bright = B[j] if j < m else POS_INF

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 0:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2.0
                return min(Aright, Bright)
            
            if Aleft > Bright:
                right = i-1
            else:
                left = i+1
        
        return -1