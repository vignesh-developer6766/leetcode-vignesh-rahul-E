# Last updated: 9/11/2026, 1:33:16 PM
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = nums1 + nums2
        arr.sort()

        n = len(arr)

        if n % 2 == 1:
            return arr[n // 2]
        else:
            middle1 = arr[n // 2 - 1]
            middle2 = arr[n // 2]

            return (middle1 + middle2) / 2