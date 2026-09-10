# Last updated: 9/10/2026, 2:56:44 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        arr = nums1 + nums2
4        arr.sort()
5
6        n = len(arr)
7
8        if n % 2 == 1:
9            return arr[n // 2]
10        else:
11            middle1 = arr[n // 2 - 1]
12            middle2 = arr[n // 2]
13
14            return (middle1 + middle2) / 2