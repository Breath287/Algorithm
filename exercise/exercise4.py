# find median binding two sorted lists
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        nums1.extend(nums2)
        nums1.sort(reverse=True)
        new_length = len(nums1)
        if new_length == 0:
            return None
        if new_length % 2 == 1:
            median = nums1[int((new_length - 1) / 2)]
            return float(median)
        else:
            median = (nums1[int((new_length)/2)] + nums1[int((new_length/2) - 1)]) / 2
            return float(median)

a = Solution().findMedianSortedArrays([1,3], [2])
print(a)














