# Binary research
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        i = (r + l) // 2  # initial A median
        j = half - i - 2  # initial B median

        Aleft, Aright = A[i], A[i+1]
        Bleft, Bright = B[j], B[j+1]

        # partition correct means we find the median
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return float(min(Aright, Bright))
            return float((max(Aleft, Bleft) + min(Aright, Bright)) / 2)
        # shift l or r to make adjustment for correct partition
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

a = Solution().findMedianSortedArrays([1,3, 5, 7], [2,3])
print(a)




