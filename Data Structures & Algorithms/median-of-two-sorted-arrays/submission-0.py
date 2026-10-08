class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        left, right = 0, m

        POS_INF = math.inf
        NEG_INF = -math.inf

        while True:
            i = (left + right) // 2
            j = half - i

            Aleft = A[i-1] if i > 0 else NEG_INF
            Aright = A[i] if i < m else POS_INF
            Bleft = B[j-1] if j > 0 else NEG_INF
            Bright = B[j] if j < n else POS_INF

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                return float(min(Aright, Bright))
            
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
        return -1
